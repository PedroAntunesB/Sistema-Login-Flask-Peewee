from flask import Blueprint, render_template, request, redirect, url_for
from database.users_database import User

user = Blueprint('user', __name__)

@user.route('/')
def login():
    return render_template('login.html')


@user.route('/acesso', methods=['GET','POST'])
def acesso_cliente():
    if request.method == 'POST':
        senha = request.form.get('password')
        email = request.form.get('email')
    if User.email == email and User.senha == senha:
        return redirect(url_for('user.conta', user_email=email))
    else:
        return redirect(url_for('user.login'))


@user.route('/<user_email>')
def conta(user_email):
    return render_template('index.html', user=User.get(User.email == user_email) )


@user.route('/criar')
def criar_conta():
    return render_template('criar_conta.html')

@user.route('/criando', methods=['POST'])
def salvar_dados():
    nomef = request.form.get('nome')
    emailf = request.form.get('email')
    senhaf = request.form.get('senha')
    enderecof = request.form.get('endereco')
    telefonef = request.form.get('telefone')

    User.create(nome=nomef, email=emailf, senha=senhaf, endereco=enderecof, telefone=telefonef)
    return redirect(url_for('user.login'))
