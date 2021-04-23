import pytest
import firebase_admin

from main_service import create_service, db


@pytest.fixture(scope='session')
def test_client():
    app = create_service()

    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='session')
def test_db():
    yield db
    firebase_admin.delete_app(db)
