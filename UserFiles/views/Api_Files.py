from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from UserFiles.controller.FilesController import FileController


class FilesApi:
    def __init__(self):
        self.file_controller = FileController()
        self.file_api = Blueprint('file_api', __name__)

    def files(self):
        @self.file_api.route('file', methods=['POST'])
        @jwt_required()
        def saveFiles():
            file = request.files['file']
            if not file:
                return jsonify({"msg": "No file part"}), 400
            return self.file_controller.saveFiles(file)

        @self.file_api.route('files', methods=['GET'])
        @jwt_required()
        def getFiles():
            return self.file_controller.getFiles()

        @self.file_api.route('file/<int:id>', methods=['DELETE'])
        @jwt_required()
        def deleteFiles(filename):
            return self.file_controller.deleteFiles(filename)

        @self.file_api.route('files/user', methods=['GET'])
        @jwt_required()
        def getFilesByUser():
            return self.file_controller.getFilesByUser()

        return self.file_api
