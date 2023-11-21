from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity
from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seeding.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///onetomany.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'A@y1992'
db = SQLAlchemy(app)

jwt = JWTManager(app)

migrate = Migrate(app, db)

from application import models
from application import routes
