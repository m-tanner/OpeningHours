from collections import deque
from datetime import time

import pytest

from src.flattener import Flattener
from src.parser import Parser
from src.validator import Validator


def test_success(good_input, good_output):
    parser = Parser()
    parsed_input = parser.parse_json_in(good_input)
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(good_output, dict)
    assert isinstance(good_output.get("output"), str)
    assert actual_output == good_output.get("output")


def test_multi(multiple_openings_same_day_input, multiple_openings_same_day_output):
    parser = Parser()
    parsed_input = parser.parse_json_in(multiple_openings_same_day_input)
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(multiple_openings_same_day_output, dict)
    assert isinstance(multiple_openings_same_day_output.get("output"), str)
    assert actual_output == multiple_openings_same_day_output.get("output")


def test_sunday_monday(sunday_to_monday_input, sunday_to_monday_output):
    parser = Parser()
    parsed_input = parser.parse_json_in(sunday_to_monday_input)
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(sunday_to_monday_output, dict)
    assert isinstance(sunday_to_monday_output.get("output"), str)
    assert actual_output == sunday_to_monday_output.get("output")


def test_all_closed(all_closed_input, all_closed_output):
    parser = Parser()
    parsed_input = parser.parse_json_in(all_closed_input)
    validator = Validator(parsed_input=parsed_input)
    validator.validate()
    flattener = Flattener(parsed_input=parsed_input)
    actual_output = flattener.flatten_to_string()

    assert isinstance(actual_output, str)
    assert isinstance(all_closed_output, dict)
    assert isinstance(all_closed_output.get("output"), str)
    assert actual_output == all_closed_output.get("output")


def test_unbalanced(unbalanced_input):
    parser = Parser()
    parsed_input = parser.parse_json_in(unbalanced_input)
    validator = Validator(parsed_input=parsed_input)

    with pytest.raises(RuntimeError):
        validator.validate()


def test_flatten_to_restaurant_fail_unbalanced():
    test_deque = deque([(time(), "monday"), (time(), "tuesday")])
    short_test_deque = deque([(time(), "monday")])
    flattener = Flattener(
        parsed_input={"openings": test_deque, "closings": short_test_deque}
    )

    with pytest.raises(RuntimeError):
        flattener.flatten_to_restaurant()
