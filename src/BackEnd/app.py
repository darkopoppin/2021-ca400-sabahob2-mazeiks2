from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from user import assignCategories
import os
import argparse


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
