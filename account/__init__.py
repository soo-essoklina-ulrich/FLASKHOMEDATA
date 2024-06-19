from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required

from account.models.User import User
from extensions import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['password'] != request.form['confirm_password']:
            flash('Les mots de passe ne correspondent pas.', 'error')
            return redirect(url_for('auth.register'))
        try:
            new_user = User(nom=request.form['nom'], prenom=request.form['prenom'], username=request.form['username'],
                            email=request.form['email'])

            new_user.set_password(request.form['password'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('inscription Echoue', 'error')

    return render_template('auth/register.html')


@auth_bp.route('', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.verify_password(password):
                login_user(user)
                flash('Authentification réussie.', 'success')
                return redirect(url_for('data.all'))
            else:
                flash('Authentification échoué.', 'error')
        except Exception as e:
            print(e)
    return render_template('auth/login.html')


@auth_bp.route('logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
