from typing import Dict, List

from flask import jsonify, request

from src.app.api import api
from src.parser import Parser


@api.route("/get_hours_for_humans", methods=["POST"])
def get_hours_for_humans():
    content: Dict[str, List[Dict[str, str]]] = request.json
    parser = Parser(json_in=content)
    return jsonify(output=parser.flatten_to_string())
