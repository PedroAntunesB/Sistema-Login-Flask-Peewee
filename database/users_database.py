from peewee import *


db = SqliteDatabase(None)

class User(Model):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    senha = CharField()
    email = CharField(unique=True)

    class Meta:
        database = db

def init_db(app):
    db.init(app.config['DATABASE'])
