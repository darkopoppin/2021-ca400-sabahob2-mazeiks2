from flask import request, Blueprint, jsonify

import settings
from service.errors import ClientError

service_bp = Blueprint("service_bp", __name__)


@service_bp.errorhandler(ClientError)
def handle_client_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@service_bp.route('/planner', methods=['GET'])
def planner():
    user_id = request.args.get('user_id')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_tim')

    return 'pass'
