from flask import request, Blueprint, jsonify
import json

from service import db
from service.errors import ClientError
from api.user_api import get_similar_users
from yelp_api.businesses import YelpGQL
from recommenders.collab_cosine import collab_cosine

service = Blueprint("service_bp", __name__)


@service.route('/recommendations', methods=['GET'])
def recommender():
    user_id = request.args.get('user_id')
    if user_id is not None:
        user = db.collection('users').document(user_id).get()
    else:
        raise ClientError("User does not exist")

    user_visited = user.to_dict().get('visited')
    if len(user_visited) != 0:
        yelp = YelpGQL()
        liked_categories = user.to_dict().get('liked_categories')
        result = yelp.search_by_categories(liked_categories)
        
    similar_users = get_similar_users(user)
    recommendations = collab_cosine(user, similar_users)

    return json.dumps(recommendations)


@service.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
