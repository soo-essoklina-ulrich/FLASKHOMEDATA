from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')



