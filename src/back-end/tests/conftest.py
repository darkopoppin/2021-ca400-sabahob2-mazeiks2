import pytest

from main_service import create_service
from firebase_admin import firestore


@pytest.fixture(scope='module')
def test_user():
    user = {
        "user_id": "test",
        "age": 21,
        "gender": "male",
        "location": "Dublin",
        "liked_categories": [
            "Hiking",
            "Parks",
            "Mountain Biking",
            "Piano Bars"],
        'visited': {}
    }
    return user


@pytest.fixture(scope='session')
def test_client():
    app = create_service()

    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='session')
def test_db():
    db = firestore.client()
    yield db
