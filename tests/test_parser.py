import json

import pytest

from src.parser import Parser


@pytest.fixture
def good_input():
    with open("tests/resources/input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def multi_input():
    with open("tests/resources/input_with_multiple_openings_same_day.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def multi_output():
    with open("tests/resources/output_with_multiple_openings_same_day.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def good_output():
    with open("tests/resources/output.json") as in_file:
        output_body = json.loads(in_file.read())
        yield output_body


@pytest.fixture
def bad_input():
    with open("tests/resources/unknown_event.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


def test_parser_fail(bad_input):
    parser = Parser(bad_input)
    with pytest.raises(RuntimeError):
        parser.flatten_to_string()


def test_parser_success(good_input, good_output):
    parser = Parser(good_input)
    actual_output = parser.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(good_output, dict)
    assert isinstance(good_output.get("output"), str)
    assert actual_output == good_output.get("output")


def test_parser_multi(multi_input, multi_output):
    parser = Parser(multi_input)
    actual_output = parser.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(multi_output, dict)
    assert isinstance(multi_output.get("output"), str)
    assert actual_output == multi_output.get("output")


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
