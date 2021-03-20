from service import app, firebase, db
from flask import request, jsonify, make_response
import pyrebase
import recommenders.collab_cosine


@app.route('/recommendations', methods=['GET'])
def recommender():
    print(request.get_json())
    return "Hello World"
