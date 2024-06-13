from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from account.models.User import User
from extensions import db

api_auth_bp = Blueprint('api_auth', __name__)


@api_auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            nom = request.json['nom']
            prenom = request.json['prenom']
            email = request.json['email']
            username = request.json['username']
            password = request.json['password']
            new_user = User(nom=nom, prenom=prenom, email=email, username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': 'Inscription réussie1'}), 201
        except Exception as e:
            return jsonify({'message': 'Inscription échouée2'}), 400
    return {'message': 'Inscription échouée3'}, 400


@api_auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.json
        try:
            username = data['username']
            password = data['password']
            user = User.query.filter_by(username=username).first()
            if user and user.verify_password(password):
                access_token = create_access_token(identity={'username': username})
                return jsonify(access_token=access_token), 200
            return jsonify({'message': 'Invalid username or password'}), 401
        except Exception as e:
            return jsonify({'message': 'Authentification échouée '}), 500
    return jsonify({'message': 'Authentification échouée '}), 401
