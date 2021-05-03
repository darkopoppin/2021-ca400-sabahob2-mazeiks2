import re
from flask import request, Blueprint, jsonify

from service import db
from service.errors import ClientError
from planner.make import create_plan

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
    try:
        if re.compile(r'^\d\d:\d\d$').match(start_time):
            start_time = start_time.split(':')
        else:
            raise ValueError
        if re.compile(r"^\d\d:\d\d$").match(end_time):
            end_time = end_time.split(':')
        else:
            raise ValueError
    except ValueError:
        raise ClientError("start_time or end_time are not in correct format")

    recommendations = request.json
    plan = create_plan(recommendations, start_time, end_time, coordinates)
    return "success"
