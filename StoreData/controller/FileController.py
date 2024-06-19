from flask import jsonify, request

from extensions import db
from StoreData.models.File import File


class FileController:
    def __init__(self):
        self.file_model = File

    def saveFile(self):
        try:
            if 'file' not in request.files:
                return jsonify({'message': 'Aucun fichier image'}), 400
            file = request.files['image']
            if file.filename == '':
                return jsonify({'message': 'Aucun fichier sélectionné'}), 400
            data = self.file_model.save_file(file)
            db.session.add(data)
            db.session.commit()
            return jsonify({'message': 'Fichier enregistrée avec succès'}), 201
        except Exception as e:
            return jsonify({'message': 'Fichier non enregistrée'}), 400

    def getFileByUser(self, userId):
        return self.file_model.get_files_by_user(userId)

    def getFile(self):
        return self.file_model.query.all()

    def deleteFile(self, fileId):
        file = self.file_model.query.get(fileId)
        db.session.delete(file)
        return db.session.commit()
