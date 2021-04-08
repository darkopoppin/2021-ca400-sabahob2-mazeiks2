from flask import Flask
import firebase_admin
from firebase_admin import firestore

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

firebase_admin.initialize_app()
db = firestore.client()

from service import service