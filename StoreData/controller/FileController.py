from extensions import db
from StoreData.models.File import File


class FileController:
    def __init__(self):
        self.file = File

    def saveFile(self, file):

        file = self.file(filename=file['filename'], filepath=file['filepath'], mimetype=file['mimetype'])
        db.session.add(file)
        return db.session.commit()

    def getFile(self):
        return self.file.query.all()

    def deleteFile(self, fileId):
        file = self.file.query.get(fileId)
        db.session.delete(file)
        return db.session.commit()