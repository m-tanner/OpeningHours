from flask import jsonify, request

from src.app.api import api


@api.route("/get_hours_for_humans", methods=["POST"])
def get_hours_for_humans():
    content = request.json
    print(content)
    return jsonify({"hi": "to_you"})
