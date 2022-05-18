from enum import Enum


class MinMax(Enum):
    MINIMUM = 'Minimum'
    MAXIMUM = 'Maximum'

    def __repr__(self) -> str:
        return f"MinMax.{self.name}"
