from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from UserFiles.models.Files import Files
from Account.models.User import User as user

from extensions import db


class FileController:
    def __init__(self):
        self.file_model = Files
        self.user_id = user

    def saveFiles(self, file):
        user_id = self.user_id.query.filter_by(username=get_jwt_identity()).first().id
        file_models = self.file_model(user_id=user_id)
        file_models.save_File(file)
        db.session.add(file_models)
        db.session.commit()
        return jsonify({
            "msg": "File created successfully",
            "filename": file.filename,
        }), 201

    def getFiles(self):
        files = self.file_model.query.all()
        result = [
            {
                "filename": file.filename,
                "created_at": file.created_at,
                "updated_at": file.updated_at,
                "user_id": file.user_id,
                "file_type": file.file_type
            } for file in files
        ]
        return jsonify(result), 200

    def deleteFiles(self, filename_id):
        file = self.file_model.query.filter_by(id=filename_id).first()
        db.session.delete(file)
        file.delete_File()
        db.session.commit()
        return jsonify({"msg": "File deleted successfully"}), 200

    def getFilesByUser(self):
        user_id = self.user_id.query.filter_by(username=get_jwt_identity()).first().id
        files = self.file_model.query.filter_by(user_id=user_id).all()
        result = [
            {
                "filename": file.filename,
                "created_at": file.created_at,
                "updated_at": file.updated_at,
                "user_id": file.user_id,
                "file_type": file.file_type
            } for file in files
        ]
        return jsonify(result), 200
