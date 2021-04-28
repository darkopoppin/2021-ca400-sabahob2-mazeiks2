from flask import request, Blueprint, jsonify
import json

from service import db
from service.errors import ClientError
from api.user_api import get_similar_users
from yelp_api.businesses import search_by_categories
from recommenders.collab_cosine import collab_cosine

service = Blueprint("service_bp", __name__)


@service.route('/recommendations', methods=['GET'])
def recommender():
    user_id = request.args.get('user_id')
    user = db.collection('users').document(user_id).get()

    if user.exists:
        user_visited = user.to_dict().get('visited')
    else:
        raise ClientError("User id does not exist")

    if len(user_visited) == 0:
        liked_categories = user.to_dict().get('liked_categories')
        result = search_by_categories(liked_categories)
        return json.dumps(result, indent=4)
    else:
        similar_users = get_similar_users(user)
        recommendations = collab_cosine(user, similar_users)
        return recommendations


@service.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
