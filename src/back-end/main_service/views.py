from flask import request, Blueprint, jsonify
from flask_cors import cross_origin
import requests

from main_service.user import assignCategories
from yelp_api.businesses import YelpGQL
from main_service.errors import ClientError

main_service = Blueprint("main_service_bp", __name__)


@main_service.errorhandler(ClientError)
def handle_clien_error(error):
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
    print(user_id)
    recommendations = requests.get(
            "http://recommender:5001/recommendations",
            params={'user_id': user_id}).json()

    # TODO:
    # Speed up the requests
    '''
    yelp = YelpGQL()

    for key in recommendations.keys():
        yelp.get_business_info(key)
    '''
    return recommendations
