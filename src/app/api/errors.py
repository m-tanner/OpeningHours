from flask import jsonify

from src.app.api import api
from src.app.exceptions import InvalidUsage


@api.errorhandler(InvalidUsage)
def invalid_usage(e):
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response
