from enum import Enum


class Bounds(Enum):
    LOWER = 'lower'
    UPPER = 'upper'

    def __repr__(self) -> str:
        return f"Bounds.{self.name}"
