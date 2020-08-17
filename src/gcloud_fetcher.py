from google.cloud import storage

from src.config_manager import ConfigManager
from src.fetcher import Fetcher


class GCloudFetcher(Fetcher):
    def __init__(self, config: ConfigManager):
        self.client = storage.Client(project=config.gcloud_project)
        self.bucket_name = config.static_bucket
        self.bucket = self.client.bucket(bucket_name=self.bucket_name)

    def fetch_image(self, icon_key: str) -> bytes:
        return self.bucket.get_blob(blob_name=icon_key).download_as_string()
