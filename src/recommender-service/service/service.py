from service import app, db
from api.user_api import get_similar_users
from recommenders.collab_cosine import collab_cosine

from flask import request
import json


@app.route('/recommendations', methods=['GET'])
def recommender():
    user_id = request.args.get('user_id')
    user = db.collection('users').document(user_id).get()
    similar_users = get_similar_users(user)
    recommendations = collab_cosine(user, similar_users)

    return json.dumps(recommendations)
