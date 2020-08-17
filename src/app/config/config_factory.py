from typing import Type

from src.app.config.config import Config
from src.app.config.config_types import key_to_type


def get_config(config_type: str) -> Type[Config]:
    return key_to_type[config_type]  # raises KeyError
