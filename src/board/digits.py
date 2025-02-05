"""Digits set for Sudoku."""
from typing import ClassVar, Iterator

from src.utils.functions import PRIMES


class Digits:
    """A class representing a digit range in a Sudoku puzzle.

    Attributes:
        minimum (int): The minimum possible digit in the range.
        maximum (int): The maximum possible digit in the range.
    """

    classes: ClassVar[dict[tuple[int, int], 'Digits']] = {}

    def __new__(cls, minimum: int, maximum: int) -> 'Digits':
        """Create a new instance or returns an existing instance if it already exists.

        Args:
            minimum (int): The minimum possible digit for the digit range.
            maximum (int): The maximum possible digit for the digit range.

        Returns:
            Digits: A new or existing instance of the Digit class.
        """
        key = (minimum, maximum)
        if key not in cls.classes:
            instance = super().__new__(cls)
            cls.classes[key] = instance
            instance.__init__(minimum, maximum)  # type: ignore[no-untyped-call, misc]
        return cls.classes[key]

    def __init__(self, minimum: int, maximum: int) -> None:
        """Initialize a new instance of the Digits class.

        Args:
            minimum (int): The minimum possible digit for the digit range.
            maximum (int): The maximum possible digit for the digit range.

        Raises:
            TypeError: If minimum or maximum is not an integer.
            ValueError: If minimum is greater than maximum.
        """
        if minimum > maximum:
            raise ValueError('Minimum must be less than or equal to maximum.')
        self.minimum: int = minimum
        self.maximum: int = maximum
        self.count: int = self.maximum - self.minimum + 1
        self.digit_range: list[int] = list(range(minimum, maximum + 1))
        self.digit_sum: int = sum(self.digit_range)
        self.primes: list[int] = [prime for prime in PRIMES if prime in self.digit_range]
        self.low: list[int] | None = None
        self.mid: list[int] | None = None
        self.high: list[int] | None = None
        self.mod0: list[int] | None = None
        self.mod1: list[int] | None = None
        self.mod2: list[int] | None = None
        if self.maximum % 3 == 0:
            chunk_size: int = self.maximum // 3
            self.low = self.digit_range[:chunk_size]
            self.mid = self.digit_range[chunk_size:chunk_size * 2]
            self.high = self.digit_range[chunk_size * 2:]
            self.mod0 = [digit for digit in self.digit_range if digit % 3 == 0]
            self.mod1 = [digit for digit in self.digit_range if digit % 3 == 1]
            self.mod2 = [digit for digit in self.digit_range if digit % 3 == 2]

        midpoint = self.count // 2
        self.lower: list[int] = self.digit_range[:midpoint]
        self.upper: list[int]
        if self.count % 2 == 0:  # Even number of digits
            self.upper = self.digit_range[midpoint:]
        else:  # Odd number of digits
            self.upper = self.digit_range[midpoint + 1:]

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
            str: A string representation of the Digits instance.
        """
        return f'{self.__class__.__name__}({self.minimum}, {self.maximum})'
