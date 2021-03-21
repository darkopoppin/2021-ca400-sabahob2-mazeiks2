from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from user import assignCategories
import os, argparse


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
    parser = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")

    parser.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")

    args = parser.parse_args()
    
    port = int(os.environ.get('PORT', 5000))
    if args.debug:
        print("Running in debug mode")
        cors = CORS(app)
        app.run(host='0.0.0.0', port=port, debug=True)
    else:
        app.run(host='0.0.0.0', port=port, debug=False)
