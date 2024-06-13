from flask import Blueprint, request, jsonify

data = Blueprint('data', __name__)

from StoreData.controller.FileController import FileController

image = FileController()


@data.route('/save')
def save():
    if request.method == 'POST':
        try:
            image.saveFile(request.files['file'])
            return jsonify({'message': 'Fichier enregistrée avec succès'}), 201
        except Exception as e:
            return jsonify({'message': e}), 500
    return jsonify({'message': 'Fichier enregistrée avec succès'}), 201


@data.route('/all')
def all():
    try:
        return image.getFile()
    except Exception as e:
        return jsonify({'message': e}), 500


@data.route('/delete/<int:id>')
def delete(id):
    try:
        return image.deleteFile(id)
    except Exception as e:
        return jsonify({'message': e}), 500
