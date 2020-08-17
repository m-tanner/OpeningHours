import pytest
from flask import current_app

from src.app import create_app


@pytest.fixture
def resource():
    app = create_app("test")
    app_context = app.app_context()
    app_context.push()
    yield "resource"
    app_context.pop()


def test_app_exists(resource):
    assert current_app is not None


def test_app_is_testing(resource):
    assert current_app.config["TESTING"]
