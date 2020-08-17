from src.config_manager import ConfigManager
from src.gcloud_fetcher import GCloudFetcher


def test_gcloud_fetcher():
    fetcher = GCloudFetcher(config=ConfigManager())

    icon = fetcher.fetch_image("my_face.jpg")
    assert isinstance(icon, bytes)
