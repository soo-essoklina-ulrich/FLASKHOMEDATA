from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from Account.models.User import User as UserModel

from extensions import db


class UserController:
    def __init__(self):
        self.model = UserModel

    def login(self, username, password):
        user = self.model.query.filter_by(username=username).first()

        if user is not None:
            if user.verify_password(password):
                access_token = create_access_token(identity=username)
                refresh_token = create_refresh_token(identity=username)
                return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
            else:
                return jsonify({"msg": "Bad username or password"}), 401
        else:
            return jsonify({"msg": "Bad username or password"}), 401

    def logout(self):
        pass

    def register(self, nom, prenom, username, password):
        user = self.model(nom=nom, prenom=prenom, username=username)
        user.password = password
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201

    def change_password(self, username, password):
        pass

    def delete_user(self, username):
        pass

    def get_user(self):
        current_user = get_jwt_identity()
        user = self.model.query.filter_by(username=current_user).first()

        return jsonify({
            "nom": user.nom,
            "prenom": user.prenom,
            "username": user.username
        }), 200

    def get_all_users(self):
        users = self.model.query.all()
        result = [
            {
                "nom": user.nom,
                "prenom": user.prenom,
                "username": user.username
            } for user in users

        ]
        return jsonify(result)
