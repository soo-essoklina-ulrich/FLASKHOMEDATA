from datetime import timedelta

from flask import Flask

from Account.views.auth_api import auth_api
from UserFiles.views.Api_Files import FilesApi
from UserFiles.views.File_Stat_Api import FileStatApi
from extensions import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

cors = CORS()

# Maintenant vous pouvez accéder aux variables d'environnement
flask_app = os.getenv('FLASK_APP')
flask_env = os.getenv('FLASK_ENV')
database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
#
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key
app.config['JWT_SECRET_KEY'] = secret_key
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Jetons d'accès expirent après 1 heure
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Jetons de rafraîchissement expirent après 30 jours


app.register_blueprint(auth_api, url_prefix='/auth/')
app.register_blueprint(FilesApi().files(), url_prefix='/api/')
app.register_blueprint(FileStatApi().stat(), url_prefix='/api/')

cors.init_app(
    app,
    resources={r"*": {"origins": "*"}}
)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from Account.models.User import User  # noqa: F401
from UserFiles.models.Files import Files  # noqa: F401

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
