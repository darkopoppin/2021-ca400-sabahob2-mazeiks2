import settings
import requests


def test_new_user(test_client, test_db):
    user_id = '9ENVClSVvVUIsJ9qSguUAjuM5213'
    response = requests.get(
        f'http://{settings.RECOMM_HOST}:5001/recommendations?user_id={user_id}')

    assert response.status_code == 200
    # New users can get up to 50 recommendations only
