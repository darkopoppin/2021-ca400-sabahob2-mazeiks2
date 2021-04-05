from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin import firestore

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

firebase_admin.initialize_app()
db = firestore.client()

from app import app