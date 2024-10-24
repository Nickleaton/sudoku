from enum import Enum


class Bounds(Enum):
    """
    An enumeration to represent bounds (lower or upper).

    Attributes:
        LOWER (str): Represents the lower bound.
        UPPER (str): Represents the upper bound.
    """
    LOWER = 'lower'
    UPPER = 'upper'

    def __repr__(self) -> str:
        """
        Returns a string representation of the Bounds enum.

        Returns:
            str: The string representation in the format 'Bounds.<name>'.
        """
        return f"Bounds.{self.name}"
