from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from UserFiles.controller.FileStatController import FileStaticController


class FileStatApi:
    def __init__(self):
        self.file_controller = FileStaticController()
        self.file_api = Blueprint('file_stat_api', __name__)

    def stat(self):
        @self.file_api.route('files/count', methods=['GET'])
        @jwt_required()
        def count_files():
            return self.file_controller.count_files()

        @self.file_api.route('files/count/user', methods=['GET'])
        @jwt_required()
        def count_files_by_user():
            return self.file_controller.count_files_by_user()

        @self.file_api.route('files/count/<string:file_type>', methods=['GET'])
        @jwt_required()
        def count_files_by_type(file_type):
            return self.file_controller.count_files_by_type(file_type)

        @self.file_api.route('files/count/user/<string:file_type>', methods=['GET'])
        @jwt_required()
        def count_files_by_user_and_type(file_type):
            return self.file_controller.count_files_by_user_and_type(file_type)

        return self.file_api
