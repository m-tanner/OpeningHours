from src.app.config.config import Config


class ProdConfig(Config):
    PREFERRED_URL_SCHEME = "https"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
