from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_cors import CORS
from Account import auth_api


app = Flask(__name__)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

CORS(app, resources={r"/*": {"origins": "*"}})
#
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



app.register_blueprint(auth_api, url_prefix='/auth')
# app.register_blueprint(api_auth_bp, url_prefix='/api/')
# app.register_blueprint(data, url_prefix='/data')
# app.register_blueprint(data_api, url_prefix='/api/file')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )
