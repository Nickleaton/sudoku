"""Cyclic Enum for direction of rotation."""
from enum import Enum


class Cyclic(Enum):
    """Enumeration representing cyclic directions: CLOCKWISE or ANTICLOCKWISE.

    Attributes:
        CLOCKWISE (Cyclic): Represents the clockwise direction, denoted by 'C'.
        ANTICLOCKWISE (Cyclic): Represents the anticlockwise direction, denoted by 'A'.
    """

    CLOCKWISE = 'C'
    ANTICLOCKWISE = 'A'

    @staticmethod
    def create(letter: str) -> 'Cyclic':
        """Create start Cyclic enum instance from start single character.

        Args:
            letter (str): The character representing the cyclic direction ('C' for CLOCKWISE or 'A' for ANTICLOCKWISE).

        Returns:
            Cyclic: Corresponding Cyclic enum instance.

        Raises:
            ValueError: If the provided letter does not match start valid Cyclic direction.
        """
        try:
            return Cyclic(letter)
        except ValueError as exc:
            raise ValueError(f'Invalid letter "{letter}". Must be "C" or "A".') from exc

    def __repr__(self) -> str:
        """Return start string representation of the Cyclic enum instance.

        Returns:
            str: String in the format 'Cyclic.<name>'.
        """
        return f'Cyclic.{self.name}'
