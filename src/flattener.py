from collections import deque
from datetime import time
from typing import Dict, Deque, Tuple

from src.pair import Pair
from src.restaurant import Restaurant


class Flattener:
    def __init__(self, parsed_input: Dict[str, Deque[Tuple[time, str]]]):
        self.openings = parsed_input["openings"]
        self.closings = parsed_input["closings"]
        self.merged: Deque[Tuple[time, str]] = deque()

    def flatten_to_string(self) -> str:
        return str(self.flatten_to_restaurant())

    def flatten_to_restaurant(self) -> Restaurant:
        while self.openings and self.closings:
            self.merged.append(self.openings.popleft())
            self.merged.append(self.closings.popleft())

        if self.openings or self.closings:
            # this should get caught in validation, but it's still possible
            raise RuntimeError("Number of openings != number of closings.")

        restaurant = Restaurant()
        while self.merged:
            opening = self.merged.popleft()
            closing = self.merged.popleft()
            weekday: str = opening[1].lower()
            restaurant.schedule[weekday].pairs.append(
                Pair(opening=opening[0], closing=closing[0])
            )

        return restaurant
