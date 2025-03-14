import os
import cloudinary
from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from datetime import timedelta
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.config["SECRET_KEY"] = 'scodilson'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False   
app.config['JWT_SECRET_KEY'] = 'omarscode007'
app.config['JWT_TOKEN_LOCATION'] = ["headers", "cookies", "json"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_COOKIE_SECURE"] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'omarscode007@gmail.com' 
app.config['MAIL_PASSWORD'] = 'zkoq dbtg cbhu usbe'
app.config['MAIL_DEFAULT_SENDER'] = 'omarscode007@gmail.com'

CORS(app)
mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)
# socketio = SocketIO(app, cors_allowed_origins="*")
serializer = URLSafeTimedSerializer('omarscode007')

cloudinary.config(
    cloud_name='do4yyqaxj',
    api_key='369969542636612',
    api_secret='xpae38WkXnOxVlmybg1WLrxJw1M'
)

from routes import auth_routes, post_route, comment_routes, reaction_routes