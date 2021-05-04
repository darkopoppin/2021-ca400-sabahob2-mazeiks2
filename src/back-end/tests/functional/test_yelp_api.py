from main_service.utils import get_recommendations


def test_get_recommendations(test_db, test_redis):
    user_id = 'myself'
    result = get_recommendations(user_id, 'planner')
    string = test_redis.get(user_id).decode('UTF-8')
    ids = string.split(' ')

    assert len(ids) == len(result.keys())
    for business, fields in result.items():
        assert len(fields) == 5
        assert 'location' in fields
        assert 'address1' in fields['location']
        assert 'rating' in fields
        assert 'categories' in fields
        assert 'parent_categories' in fields['categories'][0].keys()
