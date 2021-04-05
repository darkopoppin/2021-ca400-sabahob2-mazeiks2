from app import app
from flask import request
from flask_cors import cross_origin
from user import assignCategories


@app.route('/categorySelection', methods=['GET', 'POST'])
@cross_origin()
def userCategories():
    try:
        data = request.get_json()
        print(data)
        d = assignCategories(data)
        return d
    except Exception as e:
        print(e)
        return "not assigned"
