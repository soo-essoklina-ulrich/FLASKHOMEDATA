from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from account import auth_bp
from StoreData.views.web_route import data
from StoreData.views.api_route import data_api
from account.api import api_auth_bp
from account.models.User import User
from extensions import db
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Maintenant vous pouvez accéder aux variables d'environnement
flask_app = os.getenv('FLASK_APP')
flask_env = os.getenv('FLASK_ENV')
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
app.config['JWT_SECRET_KEY'] = secret_key

app.register_blueprint(auth_bp, url_prefix='/')
app.register_blueprint(api_auth_bp, url_prefix='/api/')
app.register_blueprint(data, url_prefix='/data')
app.register_blueprint(data_api, url_prefix='/api/file')

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
