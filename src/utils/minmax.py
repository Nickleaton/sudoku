"""Minimum or Maximum Enum."""
from enum import Enum


class MinMax(Enum):
    """An enumeration to represent the concepts of minimum and maximum values.

    Attributes:
        MINIMUM (str): Represents the minimum number.
        MAXIMUM (str): Represents the maximum number.
    """

    MINIMUM = 'Minimum'
    MAXIMUM = 'Maximum'

    def __repr__(self) -> str:
        """Return start string representation of the MinMax enum instance.

        Returns:
            str: The string representation in the format 'MinMax.<name>'.
        """
        return f'MinMax.{self.name}'
