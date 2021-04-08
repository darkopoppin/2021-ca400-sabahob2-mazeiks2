from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

CORS(app)

firebase_admin.initialize_app()
db = firestore.client()

from app import views
