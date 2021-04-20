import pytest

from service import create_service


@pytest.fixture(scope='session')
def test_client():
    app = create_service()

    with app.test_client() as client:
        with app.app_context():
            yield client
