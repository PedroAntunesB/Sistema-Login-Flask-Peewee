from flask import Blueprint, render_template, request, redirect, url_for
from database.login_acesso import USERS_LOGIN, USERS_CONTA

user = Blueprint('user', __name__)


@user.route('/')
def login():
    return render_template('login.html')


@user.route('/acesso', methods=['GET', 'POST'])
def acesso_cliente():
    if request.method == 'POST':
        tent = {request.form.get('email'): request.form.get('password')}
    for c in USERS_LOGIN:
        if c == tent:
            return redirect(url_for('user.conta', user_email= request.form.get('email')))
    return redirect(url_for('user.login'))


@user.route('/<user_email>')
def conta(user_email):
    return render_template('index.html', email=user_email, user=USERS_CONTA[user_email] )


@user.route('/criar')
def criar_conta():
    return render_template('criar_conta.html')

@user.route('/criando', methods=['POST'])
def salvar_dados():
    temp2 = {request.form.get('email') : request.form.get('senha')}
    USERS_LOGIN.append(temp2)
    USERS_CONTA[request.form.get('email')] = {'nome':request.form.get('nome'), 'id': len(USERS_CONTA), 'endereço': request.form.get('endereco'), 'telefone': request.form.get('telefone'), 'img': None}
    return redirect(url_for('user.login'))