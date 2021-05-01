from flask import request, Blueprint, jsonify
from flask_cors import cross_origin
import requests

from main_service.errors import ClientError
from yelp_api import get_businesses_info
from models.user import User
from main_service import db

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
        raise ClientError("Invalid parameter passed")
    recommendations = requests.get(
            "http://127.0.0.1:5001/recommendations",
            params={'user_id': user_id}).json()

    recommendations_ids = list(recommendations)
    results = get_businesses_info(recommendations_ids)
    return results
