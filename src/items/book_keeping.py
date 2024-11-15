"""BookKeeping."""
from typing import List
from src.utils.sudoku_exception import SudokuException


class BookKeeping:
    """Handles bookkeeping for possible values of digits in a puzzle."""

    def __init__(self, maximum_digit: int):
        """Initialize a BookKeeping instance with a maximum digit limit.

        Args:
            maximum_digit (int): The maximum digit to consider.
        """
        self.maximum_digit = maximum_digit
        self.digit_range = range(1, maximum_digit + 1)
        self.possibles = [True] * self.maximum_digit

    def __getitem__(self, digit: int) -> bool:
        """Retrieve whether a digit is possible.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is possible, False otherwise.
        """
        return self.possibles[digit - 1]

    def __setitem__(self, digit: int, value: bool) -> None:
        """Set the possibility of a digit.

        Args:
            digit (int): The digit to set.
            value (bool): The value to set, indicating if the digit is possible.
        """
        self.possibles[digit - 1] = value

    def __and__(self, other) -> 'BookKeeping':
        """Compute the logical AND of two BookKeeping instances.

        Args:
            other (BookKeeping): Another BookKeeping instance.

        Returns:
            BookKeeping: A new instance with combined possibilities.
        """
        if not isinstance(other, BookKeeping):
            raise SudokuException(f"Expected an instance of BookKeeping, got {type(other)}.")
        if self.maximum_digit != other.maximum_digit:
            raise SudokuException(f"Maximum digit mismatch: {self.maximum_digit} != {other.maximum_digit}.")
        result = BookKeeping(self.maximum_digit)
        for i in self.digit_range:
            result[i] = self[i] and other[i]
        return result

    def __or__(self, other) -> 'BookKeeping':
        """Compute the logical OR of two BookKeeping instances.

        Args:
            other (BookKeeping): Another BookKeeping instance.

        Returns:
            BookKeeping: A new instance with combined possibilities.
        """
        if not isinstance(other, BookKeeping):
            raise SudokuException(f"Expected an instance of BookKeeping, got {type(other)}.")
        if self.maximum_digit != other.maximum_digit:
            raise SudokuException(f"Maximum digit mismatch: {self.maximum_digit} != {other.maximum_digit}.")
        result = BookKeeping(self.maximum_digit)
        for i in self.digit_range:
            result[i] = self[i] or other[i]
        return result

    def __invert__(self) -> 'BookKeeping':
        """Invert the possibilities in the instance.

        Returns:
            BookKeeping: A new instance with inverted possibilities.
        """
        result = BookKeeping(self.maximum_digit)
        for i in self.digit_range:
            result[i] = not self[i]
        return result

    def __eq__(self, other) -> bool:
        """Check if two BookKeeping instances are equal.

        Args:
            other (BookKeeping): Another BookKeeping instance.

        Returns:
            bool: True if both instances have identical possibilities, False otherwise.
        """
        if not isinstance(other, BookKeeping):
            raise SudokuException(f"Expected an instance of BookKeeping, got {type(other)}.")
        if self.maximum_digit != other.maximum_digit:
            raise SudokuException(f"Maximum digit mismatch: {self.maximum_digit} != {other.maximum_digit}.")
        for i in self.digit_range:
            if self[i] != other[i]:
                return False
        return True

    def __str__(self) -> str:
        """Return a string representation of the possible digits.

        Returns:
            str: A string where possible digits are displayed, others as spaces.
        """
        return "".join([str(i) if self[i] else ' ' for i in self.digit_range])

    def __repr__(self):
        """Return a detailed string representation of the instance.

        Returns:
            str: A string showing the class name and maximum digit.
        """
        return f"{self.__class__.__name__}({self.maximum_digit!r})"

    def set_possible(self, digits: List[int]) -> None:
        """Set specific digits as possible, making others impossible.

        Args:
            digits (List[int]): The list of digits to mark as possible.
        """
        for digit in self.digit_range:
            if digit not in digits:
                self[digit] = False

    def set_impossible(self, digits: List[int]) -> None:
        """Set specific digits as impossible.

        Args:
            digits (List[int]): The list of digits to mark as impossible.
        """
        for digit in self.digit_range:
            if digit in digits:
                self[digit] = False

    def set_odd(self) -> None:
        """Set all odd digits as possible, making even digits impossible."""
        for digit in self.digit_range:
            if digit % 2 != 1:
                self[digit] = False

    def set_even(self) -> None:
        """Set all even digits as possible, making odd digits impossible."""
        for digit in self.digit_range:
            if digit % 2 != 0:
                self[digit] = False

    def set_minimum(self, lower: int) -> None:
        """Set a minimum possible digit.

        Args:
            lower (int): The lowest digit to keep as possible.
        """
        for digit in self.digit_range:
            if digit < lower:
                self[digit] = False

    def set_maximum(self, upper: int) -> None:
        """Set a maximum possible digit.

        Args:
            upper (int): The highest digit to keep as possible.
        """
        for digit in self.digit_range:
            if digit > upper:
                self[digit] = False

    def set_range(self, lower: int, upper: int) -> None:
        """Set a range of possible digits.

        Args:
            lower (int): The lowest digit to keep as possible.
            upper (int): The highest digit to keep as possible.
        """
        self.set_minimum(lower)
        self.set_maximum(upper)

    def fixed(self) -> bool:
        """Check if only one digit is marked as possible.

        Returns:
            bool: True if only one digit is possible, False otherwise.
        """
        return sum(self.possibles) == 1

    def is_possible(self, digit: int) -> bool:
        """Check if a specific digit is possible.

        Args:
            digit (int): The digit to check.

        Returns:
            bool: True if the digit is possible, False otherwise.
        """
        return self[digit]

    def is_unique(self) -> bool:
        """Check if only one digit is marked as possible.

        Returns:
            bool: True if only one digit is possible, False otherwise.
        """
        return sum(self.possibles) == 1
