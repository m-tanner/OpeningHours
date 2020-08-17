from src.config_manager import ConfigManager


def test_config_manager():
    config = ConfigManager()
    assert isinstance(config.cloud_provider, str)
    assert isinstance(config.gcloud_project, str)
    assert isinstance(config.static_bucket, str)
