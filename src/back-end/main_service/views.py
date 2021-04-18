from flask import request, Blueprint, jsonify
from flask_cors import cross_origin
import requests

from main_service.user import assignCategories
from main_service.errors import ClientError
from yelp_api import get_businesses_info

main_service = Blueprint("main_service_bp", __name__)


@main_service.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@main_service.route('/categorySelection', methods=['GET', 'POST'])
@cross_origin()
def userCategories():
    if request.is_json:
        data = request.get_json()
        d = assignCategories(data)
        return d
    else:
        raise ClientError("Expected JSON")


@main_service.route('/recommender', methods=['GET'])
@cross_origin()
def recommender():
    if 'user_id' in request.args.keys():
        user_id = request.args.get('user_id')
    else:
        raise ClientError("Invalid parameter passed")

    recommendations = requests.get(
            "http://recommender:5001/recommendations",
            params={'user_id': user_id}).json()

    recommendations_ids = list(recommendations)
    results = get_businesses_info(recommendations_ids)
    return results
