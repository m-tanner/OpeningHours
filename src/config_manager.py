import os


class ConfigManager:
    def __init__(self):
        # Raise KeyError if something is missing
        self.cloud_provider = os.environ["CLOUD_PROVIDER"]
        self.gcloud_project = os.environ["GCLOUD_PROJECT"]
        self.static_bucket = os.environ["STATIC_BUCKET"]
