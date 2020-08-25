import json

import pytest

from src.parser import Parser
from src.validator import Validator
from src.flattener import Flattener


@pytest.fixture
def good_input():
    with open("tests/resources/input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def good_output():
    with open("tests/resources/output.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture
def multi_input():
    with open("tests/resources/input_with_multiple_openings_same_day.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def multi_output():
    with open("tests/resources/output_with_multiple_openings_same_day.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture
def bad_input():
    with open("tests/resources/unknown_event.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def sunday_monday_input():
    with open("tests/resources/input_with_sunday_to_monday.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def sunday_monday_output():
    with open("tests/resources/output_with_sunday_to_monday.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture
def all_closed_input():
    with open("tests/resources/input_all_closed.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def all_closed_output():
    with open("tests/resources/output_all_closed.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture
def unbalanced_input():
    with open("tests/resources/input_unbalanced.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def bad_event_value_input():
    with open("tests/resources/input_bad_event_value.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


def test_parser_fail(bad_input):
    parser = Parser(bad_input)
    with pytest.raises(RuntimeError):
        parsed_input = parser.parse_json_in()
        validator = Validator(parsed_input=parsed_input)
        validator.validate()


def test_parser_success(good_input, good_output):
    parser = Parser(good_input)
    parsed_input = parser.parse_json_in()
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(good_output, dict)
    assert isinstance(good_output.get("output"), str)
    assert actual_output == good_output.get("output")


def test_parser_multi(multi_input, multi_output):
    parser = Parser(multi_input)
    parsed_input = parser.parse_json_in()
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(multi_output, dict)
    assert isinstance(multi_output.get("output"), str)
    assert actual_output == multi_output.get("output")


def test_parser_sunday_monday(sunday_monday_input, sunday_monday_output):
    parser = Parser(sunday_monday_input)
    parsed_input = parser.parse_json_in()
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(sunday_monday_output, dict)
    assert isinstance(sunday_monday_output.get("output"), str)
    assert actual_output == sunday_monday_output.get("output")


def test_parser_all_closed(all_closed_input, all_closed_output):
    parser = Parser(all_closed_input)
    parsed_input = parser.parse_json_in()
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(all_closed_output, dict)
    assert isinstance(all_closed_output.get("output"), str)
    assert actual_output == all_closed_output.get("output")


def test_parser_unbalanced(unbalanced_input):
    parser = Parser(unbalanced_input)
    parsed_input = parser.parse_json_in()
    validator = Validator(parsed_input=parsed_input)

    with pytest.raises(RuntimeError):
        validator.validate()


def test_parser_bad_event_value(bad_event_value_input):
    parser = Parser(bad_event_value_input)

    with pytest.raises(RuntimeError):
        parsed_input = parser.parse_json_in()
        validator = Validator(parsed_input=parsed_input)
        validator.validate()


def test_seconds_pass(good_input):
    parser = Parser(good_input)
    parser.validate_seconds(value=1)


def test_seconds_negative(good_input):
    parser = Parser(good_input)
    with pytest.raises(RuntimeError):
        parser.validate_seconds(value=-1)


def test_seconds_above_max(good_input):
    parser = Parser(good_input)
    with pytest.raises(RuntimeError):
        parser.validate_seconds(value=86400)
