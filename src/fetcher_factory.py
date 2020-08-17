from src.config_manager import ConfigManager
from src.gcloud_fetcher import GCloudFetcher


class FetcherFactory:
    def __init__(self, config: ConfigManager):
        self._config = config

    def get_fetcher(self):
        if self._config.cloud_provider == "gcloud":
            return GCloudFetcher(config=self._config)
        # other cloud providers could be added here
        raise RuntimeError(
            "CLOUD_PROVIDER was missing from your environment or "
            "didn't match any known options."
        )
