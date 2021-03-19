from flask import Flask, request, jsonify, make_response
import models.recommender

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def recommender():
    print(request.get_json())
    return "Hello World"

if __name__ == '__main__':
    app.run()