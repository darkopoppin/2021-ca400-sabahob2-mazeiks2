

def test_new_user(test_client, test_db):
    user_id = '9ENVClSVvVUIsJ9qSguUAjuM5213'
    user = test_db.collection('users').document(user_id).get()
    liked_categories = user.to_dict().get('liked_categories')

    data = dict(user_id=user_id)
    response = test_client.get('/recommendations', query_string=data)

    assert response.status_code == 200
    # New users can get up to 50 recommendations only
    assert len(response.json.keys()) <= 50

    for business, categories in response.json.items():
        assert (liked_categories[0] in categories) or (
            liked_categories[1] in categories)


def test_existing_user(test_client, test_db):
    user_id = 'KbcIgBXo6bhtfRtO6iWe'

    data = dict(user_id=user_id)
    response = test_client.get('/recommendations', query_string=data)

    assert response.status_code == 200
    for recommendation, fields in response.json.items():
        assert 'categories' in fields
        assert 'final_score' in fields
        assert 'poi_score' in fields
        assert 'user_score' in fields
