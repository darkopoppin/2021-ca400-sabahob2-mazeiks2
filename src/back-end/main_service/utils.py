import requests

import settings
from main_service import redis_client
from yelp_api import get_businesses_info


def get_recommendations(user_id):
    if redis_client.get(user_id) is not None:
        string = redis_client.get(user_id).decode('UTF-8')
        recommendations_ids = string.split(' ')
        results = get_businesses_info(recommendations_ids)
        return results

    response = requests.get(
            f'http://{settings.RECOMM_HOST}:5001/recommendations',
            params={'user_id': user_id})

    if response.status_code != 200:
        return (response.content,
                response.status_code,
                response.headers.items())

    recommendations = response.json()
    recommendations_ids = list(recommendations)

    redis_client.set(user_id, ' '.join(recommendations_ids))
    redis_client.expire(user_id, 60*60*24)

    results = get_businesses_info(recommendations_ids)
    return results
