import pytest
from flask import Flask

from main_service.views import main_service


@pytest.fixture(scope='session')
def test_client():
    app = Flask(__name__)
    app.config.from_object("config.TestingConfig")
    app.register_blueprint(main_service)

    with app.test_client() as client:
        with app.app_context():
            yield client
