def test_recommender_view(test_client):
    response = test_client.get('/recommendations')

    assert response.status_code == 400
    assert b"User id does not exist" in response.data

    data = dict(user_id='2')
    response = test_client.get('/recommendations', data=data)

    assert response.status_code == 400
    assert b"User id does not exist" in response.data
