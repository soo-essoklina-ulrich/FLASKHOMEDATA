from datetime import datetime

from extensions import db, STATIC_FOLDER
import os
import uuid
from werkzeug.utils import secure_filename

upload_folder = os.path.join(STATIC_FOLDER, 'uploads')
os.makedirs(upload_folder, exist_ok=True)


class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    filemime = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(), nullable=False, onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file_type = db.Column(db.String(50))

    def __init__(self,  user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<Files %r>' % self.filename

    def save_File(self, file):
        filename_str_uuid_uuid_ = str(uuid.uuid4()) + str(file.filename)
        filename = secure_filename(filename_str_uuid_uuid_)
        file.save(os.path.join(upload_folder, filename))
        self.filemime = file.mimetype
        self.filename = filename
        if file.mimetype.startswith('image'):
            self.file_type = 'image'
        elif file.mimetype.startswith('video'):
            self.file_type = 'video'
        elif file.mimetype.startswith('audio'):
            self.file_type = 'audio'
        else:
            self.file_type = 'other'

    def delete_File(self):
        os.remove(os.path.join(upload_folder, self.filename))
        return True
