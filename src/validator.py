from datetime import time
from typing import Dict, Deque, Tuple

from src.restaurant import Restaurant


class Validator:
    def __init__(self, parsed_input: Dict[str, Deque[Tuple[time, str]]]):
        self.openings = parsed_input.get("openings")
        self.closings = parsed_input.get("closings")
        self.merged = parsed_input.get("merged")

    def validate(self) -> bool:
        self.check_for_balance()

        self.check_for_known_days()

        return True

    def check_for_balance(self) -> None:
        if len(self.openings) != len(self.closings):
            raise RuntimeError("Number of openings != number of closings.")

    def check_for_known_days(self) -> None:
        for _, day in self.merged:
            if day not in Restaurant.schedule.keys():
                raise RuntimeError(f"{day} not supported.")
