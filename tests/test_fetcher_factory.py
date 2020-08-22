import pytest

from src.fetcher import Fetcher
from src.fetcher_factory import FetcherFactory
from src.config_manager import ConfigManager


def test_fetcher_factory_fail():
    config = ConfigManager()
    config.cloud_provider = "not_there"
    fetcher_factory = FetcherFactory(config=config)
    with pytest.raises(RuntimeError):
        fetcher_factory.get_fetcher()


def test_fetcher_factory_success():
    config = ConfigManager()
    fetcher_factory = FetcherFactory(config=config)
    fetcher = fetcher_factory.get_fetcher()
    assert isinstance(fetcher, Fetcher)
