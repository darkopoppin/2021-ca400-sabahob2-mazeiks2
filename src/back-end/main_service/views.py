import requests
from flask import request, Blueprint, jsonify
from flask_cors import cross_origin

import settings
from main_service import db
from main_service.errors import ClientError
from main_service.utils import get_recommendations
from models.user import User
from yelp_api import yelp

main_service = Blueprint("main_service_bp", __name__)


@main_service.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# Deprecated - front end handles user profile
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

    recommendations = get_recommendations(user_id, 'recommender')
    return recommendations


@main_service.route('/planner', methods=['GET'])
@cross_origin()
def planner():
    user_id = request.args.get('user_id')
    end_time = request.args.get('end_time')
    start_time = request.args.get('start_time')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if user_id is None or end_time is None or start_time is None:
        raise ClientError("No parameter/s was/were passed")

    if latitude is None or longitude is None:
        raise ClientError("Coordinates were not passed")

    recommendations = get_recommendations(user_id, 'planner')

    plan = requests.get(
            f'http://{settings.PLANNER_HOST}:5003/plan',
            params={'user_id': user_id,
                    'start_time': start_time,
                    'end_time': end_time,
                    'latitude': latitude,
                    'longitude': longitude},
            json=recommendations).json()

    return plan


@main_service.route('/search', methods=['GET'])
@cross_origin()
def search():
    if 'location' in request.args.keys() and 'term' in request.args.keys():
        location = request.args.get('location').lower()
        term = request.args.get('term').lower()
    else:
        raise ClientError("Invalid or no parameter/s was passed")

    search_results = yelp.search_yelp(term, location)
    return search_results
