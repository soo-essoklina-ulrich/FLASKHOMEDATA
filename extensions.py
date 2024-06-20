from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)

