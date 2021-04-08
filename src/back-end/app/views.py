from app import app
from flask import request
from flask_cors import cross_origin
from .user import assignCategories
from yelp_api.businesses import YelpGQL

import requests


@app.route('/categorySelection', methods=['GET', 'POST'])
@cross_origin()
def userCategories():
    if request.is_json:
        data = request.get_json()
        print(data)
        d = assignCategories(data)
        return d
    else:
        return "Request was not JSON", 400


@app.route('/recommender', methods=['GET', 'POST'])
@cross_origin()
def recommender():
    user_id = request.args.get('user_id')
    recommendations = requests.get(
            "http://127.0.0.1:5001/recommendations",
            params={'user_id': user_id}).json()

    yelp = YelpGQL()

    for key in recommendations.keys():
        yelp.get_business_info(key)
    return recommendations
