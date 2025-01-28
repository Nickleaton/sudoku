"""Digit set for Sudoku."""
from typing import Iterator


class Digit:
    """A class representing a digit range in a Sudoku puzzle.

    Attributes:
        minimum (int): The minimum possible digit in the range.
        maximum (int): The maximum possible digit in the range.
    """

    _instances: dict[tuple[int, int], 'Digit'] = {}

    def __new__(cls, minimum: int, maximum: int) -> 'Digit':
        """Create a new instance or returns an existing instance if it already exists.

        Args:
            minimum (int): The minimum possible digit for the digit range.
            maximum (int): The maximum possible digit for the digit range.

        Returns:
            Digit: A new or existing instance of the Digit class.
        """
        key = (minimum, maximum)
        if key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[key] = instance
        return cls._instances[key]

    def __init__(self, minimum: int, maximum: int) -> None:
        """Initialize a new instance of the Digit class.

        Args:
            minimum (int): The minimum possible digit for the digit range.
            maximum (int): The maximum possible digit for the digit range.

        Raises:
            TypeError: If minimum or maximum is not an integer.
            ValueError: If minimum is greater than maximum.
        """
        if not isinstance(minimum, int) or not isinstance(maximum, int):
            raise TypeError('Minimum and maximum must be integers.')
        if minimum > maximum:
            raise ValueError('Minimum must be less than or equal to maximum.')
        self.minimum: int = minimum
        self.maximum: int = maximum

    def is_valid(self, digit: int) -> bool:
        """Check if a digit is within the digit range.

        Args:
            digit (int): The digit to validate.

        Returns:
            bool: True if the digit is within the range, False otherwise.
        """
        return self.minimum <= digit <= self.maximum

    def __len__(self) -> int:
        """Return the number of possible digits in the range.

        Returns:
            int: The total number of digits in the range, inclusive.
        """
        return self.maximum - self.minimum + 1

    def __iter__(self) -> Iterator[int]:
        """Iterate over all possible digits in the range.

        Returns:
            iter: An iterator over the range of digits.
        """
        return iter(range(self.minimum, self.maximum + 1))

    def __contains__(self, digit: int) -> bool:
        """Check if a digit is within the range using the `in` operator.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is within the range, False otherwise.
        """
        return self.is_valid(digit)

    def __repr__(self) -> str:
        """Return a string representation of the instance.

        Returns:
            str: A string representation of the Digit instance.
        """
        return f'{self.__class__.__name__}(minimum={self.minimum}, maximum={self.maximum})'


digit08 = Digit(0, 8)
digit14 = Digit(1, 4)
digit16 = Digit(1, 6)
digit19 = Digit(1, 9)
digit1F = Digit(0x1, 0xF)  # noqa:N816, WPS432
