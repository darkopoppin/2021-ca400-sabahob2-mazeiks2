from service import app, db
from flask import request, jsonify, make_response
from recommenders.collab_cosine import collab_cosine
from api.user_api import get_similar_users


@app.route('/recommendations', methods=['GET'])
def recommender():
    if request.is_json:
        req = request.get_json()
        user_id = req.get('user_id')
        user = db.collection('users').document(user_id).get()
        similar_users = get_similar_users(user)
        collab_cosine(user, similar_users)
    else:
        return "Request was not JSON", 400
    return "Hello World"
