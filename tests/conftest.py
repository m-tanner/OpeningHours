import json

import pytest

from src.parser import Parser


@pytest.fixture(scope="module")
def parser():
    parser = Parser()
    yield parser


@pytest.fixture(scope="module")
def all_closed_input():
    with open("tests/resources/all_closed_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def all_closed_output():
    with open("tests/resources/all_closed_output.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture(scope="module")
def bad_day_value_input():
    with open("tests/resources/bad_day_value_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def bad_event_value_input():
    with open("tests/resources/bad_event_value_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def empty_input():
    with open("tests/resources/empty_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def good_input():
    with open("tests/resources/good_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def good_output():
    with open("tests/resources/good_output.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture(scope="module")
def missing_entry_input():
    with open("tests/resources/missing_entry_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def missing_weekday_input():
    with open("tests/resources/missing_weekday_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def multiple_openings_same_day_input():
    with open("tests/resources/multiple_openings_same_day_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def multiple_openings_same_day_output():
    with open("tests/resources/multiple_openings_same_day_output.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture(scope="module")
def sunday_to_monday_input():
    with open("tests/resources/sunday_to_monday_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def sunday_to_monday_output():
    with open("tests/resources/sunday_to_monday_output.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture(scope="module")
def time_too_high():
    with open("tests/resources/time_too_high_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def time_too_low():
    with open("tests/resources/time_too_low_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def unbalanced_input():
    with open("tests/resources/unbalanced_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture(scope="module")
def unknown_event():
    with open("tests/resources/unknown_event_input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body
