from datetime import time
from typing import Dict, Deque, Tuple

from src.restaurant import Restaurant


class Validator:
    def __init__(self, parsed_input: Dict[str, Deque[Tuple[time, str]]]):
        self.openings = parsed_input["openings"]
        self.closings = parsed_input["closings"]
        self.restaurant = Restaurant()

    def validate(self) -> None:
        self.check_for_balance()

        self.check_for_known_days()

    def check_for_balance(self) -> None:
        if len(self.openings) != len(self.closings):
            raise RuntimeError("Number of openings != number of closings.")

    def check_for_known_days(self) -> None:
        for _, day in self.openings + self.closings:
            if day not in self.restaurant.weekdays_const_time:
                raise RuntimeError(f"{day} not supported.")

    def check_for_all_days(self) -> None:
        """
        Should I require all days be present?
        Right now I "swallow" the situation where a day isn't present in the input.
        Any "missing" day is simply treated as closed.
        """
        # Add the specific missing day if this is implemented
        raise RuntimeError("All weekdays are required. You were missing one.")
