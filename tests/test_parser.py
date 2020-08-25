import pytest


def test_fail(parser, unknown_event):
    with pytest.raises(RuntimeError):
        parser.parse_json_in(unknown_event)


def test_success(parser, good_input):
    parsed_input = parser.parse_json_in(good_input)

    assert isinstance(parsed_input, dict)


def test_multi(parser, multiple_openings_same_day_input):
    parsed_input = parser.parse_json_in(multiple_openings_same_day_input)

    assert isinstance(parsed_input, dict)


def test_sunday_monday(parser, sunday_to_monday_input):
    parsed_input = parser.parse_json_in(sunday_to_monday_input)

    assert isinstance(parsed_input, dict)


def test_all_closed(parser, all_closed_input):
    parsed_input = parser.parse_json_in(all_closed_input)

    assert isinstance(parsed_input, dict)


def test_unbalanced(parser, unbalanced_input):
    parsed_input = parser.parse_json_in(unbalanced_input)

    assert isinstance(parsed_input, dict)


def test_bad_event_value(parser, bad_event_value_input):
    with pytest.raises(RuntimeError):
        parser.parse_json_in(bad_event_value_input)


def test_seconds_too_low(parser, time_too_low):
    with pytest.raises(RuntimeError):
        parser.parse_json_in(time_too_low)


def test_seconds_too_high(parser, time_too_high):
    with pytest.raises(RuntimeError):
        parser.parse_json_in(time_too_high)


def test_missing_entry(parser, missing_entry_input):
    with pytest.raises(RuntimeError):
        parser.parse_json_in(missing_entry_input)
