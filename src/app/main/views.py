import io

from flask import send_file, render_template

from src.app import fetcher
from src.app.main import main


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@main.route("/icon", methods=["GET"])
def icon():
    return send_file(
        io.BytesIO(fetcher.fetch_image("my_face.jpg")), mimetype="image/jpeg",
    )


@main.route("/health", methods=["GET"])
def health():
    return "", 200
