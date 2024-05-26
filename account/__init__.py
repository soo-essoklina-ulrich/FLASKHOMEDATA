from flask import Blueprint, request, jsonify, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required

from account.models.User import User
from extensions import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            new_user = User(nom=request.form['nom'], prenom=request.form['prenom'], username=request.form['username'])
            new_user.set_password(request.form['password'])
            new_user.is_valid_email(request.form['email'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('inscription Echoue', 'error')

    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.verify_password(password):
                login_user(user)
                flash('Authentification réussie.', 'success')
            else:
                flash('Authentification échoué.', 'error')
        except Exception as e:
            print(e)
    return render_template('auth/login.html')


@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
