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
        return jsonify({"msg": "Logged out successfully"}), 200

    def register(self, nom, prenom, username, password):
        user = self.model(nom=nom, prenom=prenom, username=username)
        user.password = password
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify(
            {"msg": "User created successfully", "access_token": access_token, "refresh_token": refresh_token}), 201

    def change_password(self, current, password, confirm):
        current_user = get_jwt_identity()
        user = self.model.query.filter_by(username=current_user).first()

        if user.verify_password(current):
            if password == confirm:
                user.password = password
                db.session.commit()
                return jsonify({"msg": "Password changed successfully"}), 200
            else:
                return jsonify({"msg": "Passwords do not match"}), 400
        else:
            return jsonify({"msg": "Bad current password"}), 400

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

    def editProfile(self, username, nom, prenom, phone, email):
        current_user = get_jwt_identity()
        user = self.model.query.filter_by(username=current_user).first()
        user.nom = nom if nom else user.nom
        user.prenom = prenom if prenom else user.prenom
        user.phone = phone if phone else user.phone
        user.email = email if email else user.email
        user.username = username if username else user.username
        db.session.commit()
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify(
            {
                "msg": "Profile updated successfully",
                "access_token": access_token,
                "refresh_token": refresh_token,
                "nom": user.nom,
                "prenom": user.prenom,
                "username": user.username
            }), 200
