from service import db
from service.errors import ClientError
from api.user_api import get_similar_users
from recommenders.collab_cosine import collab_cosine

from flask import request, Blueprint, jsonify
import json

service = Blueprint("service_bp", __name__)


@service.route('/recommendations', methods=['GET'])
def recommender():
    user_id = request.args.get('user_id')
    if user_id is not None:
        user = db.collection('users').document(user_id).get()
    else:
        raise ClientError("User does not exist")

    similar_users = get_similar_users(user)
    recommendations = collab_cosine(user, similar_users)

    return json.dumps(recommendations)


@service.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
