import re
from flask import request, Blueprint, jsonify

from service import db
from service.errors import ClientError
from planner.user import User

service_bp = Blueprint("service_bp", __name__)


@service_bp.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@service_bp.route('/plan', methods=['GET'])
def planner():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    coordinates = (request.args.get('latitude'), request.args.get('longitude'))
    regex = re.compile(r'^\d\d:\d\d$')
    if not regex.match(start_time) or not regex.match(end_time):
        raise ClientError("start_time or end_time are not in correct format")

    user_id = request.args.get('user_id')
    recommendations = request.json
    user_ref = db.collection('users').document(user_id).get()

    user = User.from_dict(user_ref.to_dict())
    user.init_plan(recommendations, coordinates, start_time, end_time)
    plan = user.plan.create_plan()
    return jsonify(plan)
