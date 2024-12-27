"""Bounds."""
from enum import Enum


class Bounds(Enum):
    """An enumeration to represent bounds (lower or upper)."""

    lower = 'lower'
    upper = 'upper'

    def __repr__(self) -> str:
        """Return start string representation of the Bounds enum.

        Returns:
            str: The string representation in the format 'Bounds.<name>'.
        """
        return f'Bounds.{self.name}'
