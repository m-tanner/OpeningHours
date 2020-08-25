from typing import Dict, List

from flask import jsonify, request

from src.flattener import Flattener
from src.app.exceptions import InvalidUsage
from src.app.api import api
from src.parser import Parser
from src.validator import Validator


@api.route("/get_hours_for_humans", methods=["POST"])
def get_hours_for_humans():
    try:
        content: Dict[str, List[Dict[str, str]]] = request.json

        parser = Parser(json_in=content)
        parsed_input = parser.parse_json_in()

        validator = Validator(parsed_input=parsed_input)
        validator.validate()

        flattener = Flattener(parsed_input=parsed_input)
        return jsonify(output=flattener.flatten_to_string())
    except RuntimeError as err:
        raise InvalidUsage(str(err), status_code=400)
