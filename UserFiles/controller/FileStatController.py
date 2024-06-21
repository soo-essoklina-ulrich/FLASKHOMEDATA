from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from UserFiles.models.Files import Files
from Account.models.User import User as user

from extensions import db


class FileStaticController:

    def __init__(self):
        self.file = Files
        self.user_id = user

    def count_files(self):
        files = self.file.query.all()
        return len(files)

    def count_files_by_user(self):
        user_id = self.user_id.query.filter_by(username=get_jwt_identity()).first().id
        files = self.file.query.filter_by(user_id=user_id).all()
        return len(files)

    def count_files_by_type(self, file_type):
        files = self.file.query.filter_by(file_type=file_type).all()
        return len(files)

    def count_files_by_user_and_type(self, file_type):
        user_id = self.user_id.query.filter_by(username=get_jwt_identity()).first().id
        files = self.file.query.filter_by(user_id=user_id, file_type=file_type).all()
        return len(files)
