import json

from src.human_formatter import get_for_human


def test_human_formatter():
    with open("tests/resources/input.json") as in_file:
        input_body = json.loads(in_file.read())

    with open("tests/resources/output.json") as in_file:
        output_body = json.loads(in_file.read())

    assert get_for_human(input_body) == output_body
