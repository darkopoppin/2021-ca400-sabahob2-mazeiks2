from flask import Flask
import pyrebase

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

firebase = pyrebase.initialize_app(app.config["FIREBASE_CONFIG"])
db = firebase.database()

from service import service