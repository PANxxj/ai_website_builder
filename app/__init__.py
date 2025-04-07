from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
import ssl
from app.extension import mongo,bcrypt,jwt
import certifi
from pymongo import MongoClient


# mongo = PyMongo()
# bcrypt = Bcrypt()
# jwt = JWTManager()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)
    app.config.from_object("app.config.Config")
    mongo.cx = MongoClient(os.getenv("MONGO_URI"), tlsCAFile=certifi.where())

    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.website import website_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(website_bp, url_prefix="/api/websites")

    return app
