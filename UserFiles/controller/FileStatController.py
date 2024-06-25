import psutil
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from UserFiles.models.Files import Files
from Account.models.User import User as user

from extensions import db, BASE_DIR


class FileStaticController:

    def __init__(self):
        self.file = Files
        self.user_id = user

    def count_files(self):
        files = self.file.query.all()
        return {"len": len(files)}

    def count_files_by_user(self):
        user_id = self.user_id.query.filter_by(username=get_jwt_identity()).first().id
        files = self.file.query.filter_by(user_id=user_id).all()
        return {"len": len(files)}

    def count_files_by_type(self, file_type):
        files = self.file.query.filter_by(file_type=file_type).all()
        return {"len": len(files)}

    def count_files_by_user_and_type(self, file_type):
        user_id = self.user_id.query.filter_by(username=get_jwt_identity()).first().id
        files = self.file.query.filter_by(user_id=user_id, file_type=file_type).all()
        return {"len": len(files)}

    def count_all_file_by_type(self):
        image = self.file.query.filter_by(file_type='image').all()
        video = self.file.query.filter_by(file_type='video').all()
        audio = self.file.query.filter_by(file_type='audio').all()
        return {
            "image": len(image),
            "video": len(video),
            "audio": len(audio)
        }

    def diskuage(self):
        usage = psutil.disk_usage(BASE_DIR)
        total = round(usage.total / (1024 ** 3), 2)
        used = round(usage.used / (1024 ** 3), 2)
        free = round(usage.free / (1024 ** 3), 2)
        percent = usage.percent
        return {
            'total': total,
            'used': used,
            'free': free,
            'percent': percent
        }
