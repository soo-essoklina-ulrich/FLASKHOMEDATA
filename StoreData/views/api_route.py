from flask import Blueprint, jsonify

data_api = Blueprint('data_api', __name__)

from StoreData.controller.FileController import FileController

image = FileController()


@data_api.route('/save', methods=['POST'])
def save():
    return image.saveFile()


@data_api.route('/all')
def allimageimage():
    return image.getFile()


@data_api.route('/delete/<int:id>')
def delete(id):
    return image.deleteFile(id)
