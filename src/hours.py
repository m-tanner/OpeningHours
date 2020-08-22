from dataclasses import dataclass, field
from datetime import time
from typing import List


@dataclass
class Pair:
    opening: time
    closing: time

    def __repr__(self) -> str:
        return f"{self.get_time_as_string(self.opening)} - {self.get_time_as_string(self.closing)}"

    def get_time_as_string(self, the_time: time) -> str:
        return self.get_time_without_padding(the_time.strftime("%I %p"))

    @staticmethod
    def get_time_without_padding(padded_time: str) -> str:
        return padded_time.lstrip("0").replace(" 0", " ")


@dataclass
class Hours:
    pairs: List[Pair] = field(default_factory=list)

    def __repr__(self) -> str:
        if not self.pairs:
            return "Closed"
        return ", ".join([str(pair) for pair in self.pairs])
