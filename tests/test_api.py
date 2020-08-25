import json

import pytest

from src.app import create_app


@pytest.fixture(autouse=True)
def app():
    app = create_app("test")
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


@pytest.fixture
def test_client(app):
    with app.test_client() as test_client:
        yield test_client


def get_headers():
    return {"Accept": "application/json", "Content-Type": "application/json"}


def test_404(test_client):
    response = test_client.get("wrong/url", headers=get_headers())
    assert response.status_code == 404


def test_unknown_event(test_client, unknown_event):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(unknown_event),
    )
    assert response.status_code == 400
    assert response.json.get("message") == "Unknown event type provided."


def test_unbalanced(test_client, unbalanced_input):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(unbalanced_input),
    )
    assert response.status_code == 400
    assert response.json.get("message") == "Number of openings != number of closings."


def test_bad_event_value(test_client, bad_event_value_input):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(bad_event_value_input),
    )
    assert response.status_code == 400
    assert response.json.get("message") == "Event value (time) required. Can't be null."


def test_seconds_too_low(test_client, time_too_low):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(time_too_low),
    )
    assert response.status_code == 400
    assert response.json.get("message") == "Seconds cannot be less than 0."


def test_seconds_too_high(test_client, time_too_high):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(time_too_high),
    )
    assert response.status_code == 400
    assert response.json.get("message") == "Seconds cannot be greater than 86399."


def test_bad_day_value(test_client, bad_day_value_input):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(bad_day_value_input),
    )
    assert response.status_code == 400
    assert response.json.get("message") == "eigthday not supported."


def test_success(test_client, good_input, good_output):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(good_input),
    )
    assert response.status_code == 200
    assert response.json == good_output


def test_multi(
    test_client, multiple_openings_same_day_input, multiple_openings_same_day_output
):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(multiple_openings_same_day_input),
    )
    assert response.status_code == 200
    assert response.json == multiple_openings_same_day_output


def test_sunday_monday(test_client, sunday_to_monday_input, sunday_to_monday_output):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(sunday_to_monday_input),
    )
    assert response.status_code == 200
    assert response.json == sunday_to_monday_output


def test_all_closed(test_client, all_closed_input, all_closed_output):
    response = test_client.post(
        "api/v1/get_hours_for_humans",
        headers=get_headers(),
        data=json.dumps(all_closed_input),
    )
    assert response.status_code == 200
    assert response.json == all_closed_output
