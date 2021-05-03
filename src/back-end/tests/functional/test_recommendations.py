

def test_new_user(test_client, test_db, test_redis):
    user_id = '9ENVClSVvVUIsJ9qSguUAjuM5213'

    before_cache = obtain_recommendations(user_id, test_client, test_db)
    compare_result_and_cached(user_id, before_cache, test_client, test_redis)


def test_existing_user(test_client, test_db, test_redis):
    user_id = 'myself'

    before_cache = obtain_recommendations(user_id, test_client, test_db)
    compare_result_and_cached(user_id, before_cache, test_client, test_redis)


def obtain_recommendations(user_id, test_client, test_db):
    data = dict(user_id=user_id)
    response = test_client.get('/recommender', query_string=data)
    assert response.status_code == 200
    for key, business in response.json.items():
        assert key.find('b') == 0
        assert 'name' in business.keys()
        assert 'id' in business.keys()
        assert 'location' in business.keys()
        assert 'rating' in business.keys()

    return response.json


def compare_result_and_cached(user_id, before_cache, test_client, test_redis):
    assert test_redis.get(user_id) is not None
    data = dict(user_id=user_id)
    response = test_client.get('/recommender', query_string=data)

    assert len(before_cache) == len(response.json)
    for old, cached in zip(before_cache.keys(), response.json.keys()):
        assert old == cached
