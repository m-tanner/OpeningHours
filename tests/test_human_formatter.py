import json

from src.human_formatter import get_for_human


def test_human_formatter():
    with open("tests/resources/input.json") as in_file:
        input_body = json.loads(in_file.read())

    with open("tests/resources/output.json") as in_file:
        verified_output = json.loads(in_file.read())

    actual_output = get_for_human(input_body)

    assert isinstance(actual_output, str)
    assert isinstance(verified_output, dict)
    assert isinstance(verified_output.get("output"), str)
    assert actual_output == verified_output.get("output")


if __name__ == "__main__":
    test_human_formatter()
