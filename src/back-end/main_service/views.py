import requests
from flask import request, Blueprint, jsonify
from flask_cors import cross_origin

import settings
from main_service import redis_client, db
from main_service.errors import ClientError
from models.user import User
from yelp_api import get_businesses_info, search_yelp

main_service = Blueprint("main_service_bp", __name__)


@main_service.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@main_service.route('/user_profile', methods=['GET', 'POST'])
@cross_origin()
def user_profile():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
        user_id = data.get('user_id')
        existing_user = db.collection('users').document(user_id).get()
        if existing_user.exists:
            user = User.from_dict(user_id, existing_user.to_dict())
            categories = data.get('liked_categories')
            user.updateCategories(categories)
            user.save(categories=True)
        else:
            user = User(
                data['user_id'],
                data['age'],
                data['gender'],
                data['location'],
                data['liked_categories']
            )
            user.save()
    else:
        raise ClientError("Expected JSON")

    if request.method == 'GET':
        return 'pass'


# TODO handle empty recommendations
@main_service.route('/recommender', methods=['GET'])
@cross_origin()
def recommender():
    if 'user_id' in request.args.keys():
        user_id = request.args.get('user_id')
    else:
        raise ClientError("Invalid or no parameter/s was passed")

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


@main_service.route('/search', methods=['GET'])
@cross_origin()
def search():
    if 'location' in request.args.keys() and 'term' in request.args.keys():
        location = request.args.get('location').lower()
        term = request.args.get('term').lower()
    else:
        raise ClientError("Invalid or no parameter/s was passed")

    search_results = search_yelp(term, location)
    return search_results
