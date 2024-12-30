from flask import Flask, send_from_directory
from routes.rotas import user

app = Flask(__name__)

app.register_blueprint(user)

app.run(debug=True)
