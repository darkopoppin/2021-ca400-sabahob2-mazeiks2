import pytest
import json
from os import path

from service import create_service
from firebase_admin import firestore


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


@pytest.fixture(scope='module')
def test_recommended():
    with open(str(path.dirname(__file__)) + '/recommended.json') as f:
        yield json.load(f)


@pytest.fixture(scope='module')
def test_user(test_db):
    user_ref = test_db.collection(
        'users').document('FBUmHzsMQcEl6KAiAzNB').get()
    yield user_ref.to_dict()
    del user_ref
