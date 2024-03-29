import os

from waitress import serve

from src.app import create_app


def start_serving():
    app = create_app(os.getenv("FLASK_CONFIG"))
    serve(app, listen="*:8080")


if __name__ == "__main__":
    start_serving()
