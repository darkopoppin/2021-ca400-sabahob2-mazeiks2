import firebase_admin
import redis
from firebase_admin import firestore
from flask import Flask

import settings


firebase_admin.initialize_app()
db = firestore.client()
redis_client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASS)


def init_blueprints(app):
    from service.views import service_bp

    app.register_blueprint(service_bp)


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
