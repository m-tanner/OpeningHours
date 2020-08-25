import logging
from typing import Dict, List

from flask import jsonify, request

from src.app.api import api
from src.app.exceptions import InvalidUsage
from src.flattener import Flattener
from src.parser import Parser
from src.validator import Validator


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


@api.route("/get_hours_for_humans", methods=["POST"])
def get_hours_for_humans():
    try:
        content: Dict[str, List[Dict[str, str]]] = request.json
        logger.log(level=logging.INFO, msg=content)

        parser = Parser()
        parsed_input = parser.parse_json_in(json_in=content)

        validator = Validator(parsed_input=parsed_input)
        validator.validate()

        flattener = Flattener(parsed_input=parsed_input)

        result = flattener.flatten_to_string()
        logger.log(level=logging.INFO, msg=result.replace("\n", " "))
        return jsonify(output=result)
    except RuntimeError as err:
        logger.log(level=logging.INFO, msg=err)
        raise InvalidUsage(str(err), status_code=400)
