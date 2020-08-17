import abc
import os


class Config(metaclass=abc.ABCMeta):
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "hard to guess string")
    DEBUG = False
    TESTING = False

    @staticmethod
    def init_app(app):
        pass
