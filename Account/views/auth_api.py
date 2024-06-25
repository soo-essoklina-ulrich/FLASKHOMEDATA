from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from Account.controller.UserController import UserController

auth_api = Blueprint('auth_api', __name__)

user_controller = UserController()


@auth_api.route('login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    print(username, password)
    return user_controller.login(username, password)


@auth_api.route('register', methods=['POST'])
def register():
    nom = request.json.get('nom', None)
    prenom = request.json.get('prenom', None)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not nom or not prenom or not username or not password:
        return {"msg": "Missing required fields"}, 400
    return user_controller.register(nom, prenom, username, password)


@auth_api.route('user', methods=['GET'])
@jwt_required()
def get_user():
    return user_controller.get_user()


@auth_api.route('change_password', methods=['POST'])
@jwt_required()
def change_password():
    currentpassword = request.json.get('currentpassword', None)
    password = request.json.get('password', None)
    confirm = request.json.get('confirm', None)
    if not password or not confirm:
        return {"msg": "Missing required fields"}, 400
    return user_controller.change_password(currentpassword, password, confirm)


@auth_api.route('profile', methods=['PUT'])
@jwt_required()
def profile():
    username = request.json.get('username', None)
    nom = request.json.get('nom', None)
    prenom = request.json.get('prenom', None)
    phone = request.json.get('phone', None)
    email = request.json.get('email', None)
    return user_controller.editProfile(username, nom, prenom, phone, email)


@auth_api.route('logout', methods=['GET'])
@jwt_required()
def logout():
    return user_controller.logout()
