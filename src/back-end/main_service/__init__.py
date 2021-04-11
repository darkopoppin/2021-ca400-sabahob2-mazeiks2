from flask import Flask
import firebase_admin
from firebase_admin import firestore
from main_service.views import main_service

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

app.register_blueprint(main_service)

firebase_admin.initialize_app()
db = firestore.client()
