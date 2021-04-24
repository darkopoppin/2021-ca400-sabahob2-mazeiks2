import pytest
import firebase_admin

from main_service import create_service
from firebase_admin import firestore


@pytest.fixture(scope='session')
def test_client():
    app = create_service()

    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='session')
def test_db():
    app = firebase_admin.initialize_app()
    db = firestore.client(app)
    yield db
    firebase_admin.delete_app(app)
