import firebase_admin
from firebase_admin import firestore
from flask import Flask


firebase_admin.initialize_app()
db = firestore.client()


def init_blueprints(app):
    from service.views import service

    app.register_blueprint(service)


def create_service():
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    init_blueprints(app)
    return app
