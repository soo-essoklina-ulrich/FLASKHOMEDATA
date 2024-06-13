import os
from datetime import datetime
import uuid
from werkzeug.utils import secure_filename
from extensions import db

upload_folder = os.path.join('static', 'file')
os.makedirs(upload_folder, exist_ok=True)


class File(db.Model):
    __tablename__='file'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(256), nullable=False)
    filepath = db.Column(db.String(512), nullable=False)
    mimetype = db.Column(db.String(128), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('file', lazy=True))

    def __init__(self, filename, filepath, mimetype):
        self.filename = filename
        self.filepath = filepath
        self.mimetype = mimetype

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def save_file(self, file):
        if file:
            self.filename = secure_filename(file.filename+uuid.uuid4())
            self.filepath = os.path.join(upload_folder, self.filename)
            self.mimetype = file.mimetype
            file.save(self.filepath)
            db.session.commit()

    def __str__(self):
        return self.filename

    def __repr__(self):
        return f'<file {self.filename}>'
