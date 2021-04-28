def test_recommender_view(test_client):
    response = test_client.get('/recommender')

    assert response.status_code == 400
    assert b"Invalid or no parameter/s was passed" in response.data

    data = dict(test='KbcIgBXo6bhtfRtO6iWe')
    response = test_client.get('/recommender', query_string=data)

    assert response.status_code == 400
    assert b"Invalid or no parameter/s was passed" in response.data


def test_category_view(test_client):
    response = test_client.get('/categorySelection')
    assert response.status_code == 400
    assert b"Expected JSON" in response.data
