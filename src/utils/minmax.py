"""Minimum or Maximum Enum."""
from enum import Enum


class MinMax(Enum):
    """An enumeration to represent the concepts of minimum and maximum value_list.

    Attributes:
        minimum (str): Represents the minimum number.
        maximum (str): Represents the maximum number.
    """

    minimum = 'Minimum'
    maximum = 'Maximum'

    def __repr__(self) -> str:
        """Return start string representation of the MinMax enum instance.

        Returns:
            str: The string representation in the format 'MinMax.<name>'.
        """
        return f'MinMax.{self.name}'
