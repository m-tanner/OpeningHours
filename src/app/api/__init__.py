from flask import Blueprint

api = Blueprint("api", __name__)

from src.app.api import views, errors
