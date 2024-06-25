import os
import uuid

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from extensions import db, STATIC_FOLDER

upload_folder = os.path.join(STATIC_FOLDER, 'profile')
os.makedirs(upload_folder, exist_ok=True)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(80), nullable=False)
    prenom = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.Integer, unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    files = db.relationship('Files', backref='user', lazy=True)

    def __init__(self, nom, prenom, username):
        self.nom = nom
        self.prenom = prenom
        self.username = username

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def saveimageProfile(self, file):
        filename_str_uuid_uuid_ = str(uuid.uuid4()) + str(file.filename)
        filename = secure_filename(filename_str_uuid_uuid_)
        file.save(os.path.join(upload_folder, filename))
        self.image = filename

    def delete_Image(self):
        os.remove(os.path.join(upload_folder, self.filename))
        return True

    def __repr__(self):
        return f'<User {self.username}>'
