from typing import Dict, List

from src.parser import Parser


def get_for_human(cryptic_json: Dict[str, List[Dict[str, str]]]) -> str:
    parser = Parser(json_in=cryptic_json)
    return str(parser.flatten_to_restaurant())
