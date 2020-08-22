from flask import jsonify, request

from src.human_formatter import get_for_human
from src.app.api import api


@api.route("/get_hours_for_humans", methods=["POST"])
def get_hours_for_humans():
    content = request.json
    return jsonify(output=get_for_human(content))
