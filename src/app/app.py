import os

import click

from src.app import create_app

app = create_app(os.getenv("FLASK_CONFIG", "default"))


@app.cli.command()
@click.argument("pytest_arg", nargs=-1)
def test(pytest_arg):
    import pytest

    if not pytest_arg:
        pytest.main(["-x", "-s", "-v", "--disable-pytest-warnings", "tests/"])
    else:
        pytest.main([f"tests/{str(pytest_arg[0])}"])
