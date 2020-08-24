from dataclasses import dataclass, field
from typing import List

from src.pair import Pair


@dataclass
class Hours:
    pairs: List[Pair] = field(default_factory=list)

    def __repr__(self) -> str:
        if not self.pairs:
            return "Closed"
        return ", ".join([str(pair) for pair in self.pairs])
