import json

import pytest

from src.human_formatter import get_for_human


@pytest.fixture
def good_input():
    with open("tests/resources/input.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


@pytest.fixture
def bad_input():
    with open("tests/resources/unknown_event.json") as in_file:
        input_body = json.loads(in_file.read())
        yield input_body


def test_parser_fail(bad_input):
    with pytest.raises(RuntimeError):
        get_for_human(bad_input)


def test_parser_success(good_input):
    assert isinstance(get_for_human(good_input), str)
