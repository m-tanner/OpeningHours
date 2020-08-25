from datetime import time
from typing import Dict, Deque, Tuple

from src.pair import Pair
from src.restaurant import Restaurant


class Flattener:
    def __init__(self, parsed_input: Dict[str, Deque[Tuple[time, str]]]):
        self.openings = parsed_input.get("openings")
        self.closings = parsed_input.get("closings")
        self.merged = parsed_input.get("merged")

    def flatten_to_string(self) -> str:
        return str(self.flatten_to_restaurant())

    def flatten_to_restaurant(self) -> Restaurant:
        while self.openings or self.closings:
            self.merged.append(self.openings.popleft())
            self.merged.append(self.closings.popleft())

        restaurant = Restaurant()
        while self.merged:
            opening = self.merged.popleft()
            closing = self.merged.popleft()
            weekday: str = opening[1].lower()
            # TODO they tested an "eigthday" that broke here
            restaurant.schedule[weekday].pairs.append(
                Pair(opening=opening[0], closing=closing[0])
            )

        return restaurant
