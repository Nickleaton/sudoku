from enum import Enum


class Cyclic(Enum):
    """
    An enumeration to represent cyclic directions: CLOCKWISE or ANTICLOCKWISE.

    Attributes:
        CLOCKWISE (str): Represents the clockwise direction, indicated by 'C'.
        ANTICLOCKWISE (str): Represents the anticlockwise direction, indicated by 'A'.
    """
    CLOCKWISE = 'C'
    ANTICLOCKWISE = 'A'

    @staticmethod
    def create(letter: str) -> 'Cyclic':
        """
        Creates a Cyclic enum instance from a single letter.

        Args:
            letter (str): The letter representing the cyclic direction ('C' or 'A').

        Returns:
            Cyclic: The corresponding Cyclic enum.

        Raises:
            ValueError: If the letter is not valid.
        """
        return Cyclic(letter)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Cyclic enum.

        Returns:
            str: The string representation in the format 'Cyclic.<name>'.
        """
        return f"Cyclic.{self.name}"
