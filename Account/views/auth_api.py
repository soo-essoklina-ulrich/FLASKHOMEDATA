from Account import auth_api

from Account.controller.UserController import UserController
from flask import request
from flask_jwt_extended import jwt_required

user_controller = UserController()


@auth_api.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    return user_controller.login(username, password)


@auth_api.route('/register', methods=['POST'])
def register():
    nom = request.json.get('nom', None)
    prenom = request.json.get('prenom', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    return user_controller.register(nom, prenom, username, password)


@auth_api.route('/user', methods=['GET'])
@jwt_required
def get_user():
    return user_controller.get_user()
