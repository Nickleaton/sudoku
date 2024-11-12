"""Bounds."""
from enum import Enum


class Bounds(Enum):
    """An enumeration to represent bounds (lower or upper)."""

    LOWER = 'lower'
    UPPER = 'upper'

    def __repr__(self) -> str:
        """
        Return a string representation of the Bounds enum.

        Returns:
            str: The string representation in the format 'Bounds.<name>'.
        """
        return f"Bounds.{self.name}"
