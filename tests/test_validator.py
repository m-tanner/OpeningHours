import pytest

from src.validator import Validator


def test_unbalanced(parser, unbalanced_input):
    parsed_input = parser.parse_json_in(unbalanced_input)
    validator = Validator(parsed_input=parsed_input)

    with pytest.raises(RuntimeError):
        validator.validate()


def test_bad_day_value(parser, bad_day_value_input):
    parsed_input = parser.parse_json_in(bad_day_value_input)
    validator = Validator(parsed_input=parsed_input)

    with pytest.raises(RuntimeError):
        validator.validate()


def test_all_days_present(parser, empty_input):
    parsed_input = parser.parse_json_in(empty_input)
    validator = Validator(parsed_input=parsed_input)

    with pytest.raises(RuntimeError):
        validator.check_for_all_days()
