import os

from flask import Flask
from flask_bootstrap import Bootstrap

from src.app.config import config, config_factory
from src.config_manager import ConfigManager
from src.fetcher_factory import FetcherFactory

config_manager = ConfigManager()
fetcher = FetcherFactory(config=config_manager).get_fetcher()


def create_app(config_type: str) -> Flask:
    app = Flask(__name__.split(".")[0], root_path=os.path.join(os.getcwd(), "src/app"))
    app_config = config_factory.get_config(config_type)
    app.config.from_object(app_config)

    app_config.init_app(app)
    Bootstrap(app)

    from src.app.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from src.app.api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app
