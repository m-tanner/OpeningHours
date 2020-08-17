import abc


class Fetcher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_image(self, icon_key: str) -> bytes:
        raise NotImplementedError
