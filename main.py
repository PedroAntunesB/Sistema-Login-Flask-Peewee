from flask import Flask
from routes.rotas import user
from database.users_database import db, User, init_db

app = Flask(__name__)

app.config['DATABASE'] = 'Users.db'

init_db(app)

with db:
    db.create_tables([User])

app.register_blueprint(user)

@app.before_request
def before_request():
    if db.is_closed():
        db.connect()

@app.teardown_request
def teardown_request(exception):
    if not db.is_closed():
        db.close()

app.run(debug=True)
