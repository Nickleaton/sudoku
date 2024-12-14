"""BookKeepingCell."""
from src.utils.sudoku_exception import SudokuException


class BookKeepingCell:  # noqa: WPS214
    """Handles bookkeeping for possible values of digits in a puzzle."""

    def __init__(self, maximum_digit: int) -> None:
        """Initialize a BookKeepingCell instance with a maximum digit limit.

        Args:
            maximum_digit (int): The maximum digit to consider.
        """
        self.maximum_digit: int = maximum_digit
        self.digit_range: range = range(1, maximum_digit + 1)
        self.possibles: list[bool] = [True for _ in range(self.maximum_digit)]

    def __getitem__(self, digit: int) -> bool:
        """Determine if a digit is possible.

        Args:
            digit (int): The digit to be checked.

        Returns:
            bool: True if the digit is possible; False otherwise.

        Raises:
            SudokuException: If the digit is invalid (less than 1 or greater than the maximum allowed digit).
        """
        if digit - 1 < 0 or digit > self.maximum_digit:
            raise SudokuException(f'Invalid digit: {digit}.')
        return self.possibles[digit - 1]

    def __setitem__(self, digit: int, digit_value: bool) -> None:
        """Set whether a digit is possible.

        Args:
            digit (int): The digit to be updated.
            digit_value (bool): The digit to be assigned, indicating if the digit is possible.

        Raises:
            SudokuException: If the digit is invalid (less than 1 or greater than the maximum allowed digit).
        """
        if digit - 1 < 0 or digit > self.maximum_digit:
            raise SudokuException(f'Invalid digit: {digit}.')
        self.possibles[digit - 1] = digit_value

    def __and__(self, other: 'BookKeepingCell') -> 'BookKeepingCell':
        """Compute the logical AND of two BookKeepingCell instances.

        Args:
            other (BookKeepingCell): Another BookKeepingCell instance to combine with.

        Returns:
            BookKeepingCell: A new instance with the combined possibilities from both cells.

        Raises:
            SudokuException: If the other instance is not a BookKeepingCell
                or if there is a mismatch in the maximum digit.
        """
        if not isinstance(other, BookKeepingCell):
            raise SudokuException(f'Expected an instance of BookKeepingCell, got {type(other)}.')
        if self.maximum_digit != other.maximum_digit:
            raise SudokuException(f'Maximum digit mismatch: {self.maximum_digit} != {other.maximum_digit}.')
        combined_cell: BookKeepingCell = BookKeepingCell(self.maximum_digit)
        for digit in self.digit_range:
            combined_cell[digit] = self[digit] and other[digit]
        return combined_cell

    def __or__(self, other: 'BookKeepingCell') -> 'BookKeepingCell':
        """Compute the logical OR of two BookKeepingCell instances.

        Args:
            other (BookKeepingCell): Another BookKeepingCell instance to combine with.

        Returns:
            BookKeepingCell: A new instance with the combined possibilities from both cells.

        Raises:
            SudokuException: If the other instance is not a BookKeepingCell
                or if there is a mismatch in the maximum digit.
        """
        if not isinstance(other, BookKeepingCell):
            raise SudokuException(f'Expected an instance of BookKeepingCell, got {type(other)}.')
        if self.maximum_digit != other.maximum_digit:
            raise SudokuException(f'Maximum digit mismatch: {self.maximum_digit} != {other.maximum_digit}.')
        combined_cell: BookKeepingCell = BookKeepingCell(self.maximum_digit)
        for digit in self.digit_range:
            combined_cell[digit] = self[digit] or other[digit]
        return combined_cell

    def __invert__(self) -> 'BookKeepingCell':
        """Invert the possibilities in the instance.

        Returns:
            BookKeepingCell: A new instance with inverted possibilities.
        """
        inverted_cell: BookKeepingCell = BookKeepingCell(self.maximum_digit)
        for digit in self.digit_range:
            inverted_cell[digit] = not self[digit]
        return inverted_cell

    def __eq__(self, other: object) -> bool:
        """Check if two BookKeepingCell instances are equal.

        Args:
            other (object): Another object to compare.

        Returns:
            bool: True if both instances have identical possibilities; False otherwise.

        Raises:
            SudokuException: If the other instance is a BookKeepingCell and
                there is a mismatch in the maximum digit.
        """
        if not isinstance(other, BookKeepingCell):
            return False
        if self.maximum_digit != other.maximum_digit:
            raise SudokuException(f'Maximum digit mismatch: {self.maximum_digit} != {other.maximum_digit}.')
        for digit in self.digit_range:
            if self[digit] != other[digit]:
                return False
        return True

    def __str__(self) -> str:
        """Return a string representation of the possible digits.

        Returns:
            str: A string where possible digits are displayed, others as spaces.
        """
        digits: list[str] = [str(digit) if self[digit] else ' ' for digit in self.digit_range]
        return ''.join(digits)

    def __repr__(self) -> str:
        """Return a detailed string representation of the instance.

        Returns:
            str: A string showing the class name and maximum digit.
        """
        return f'{self.__class__.__name__}({self.maximum_digit!r})'

    def __len__(self) -> int:
        """Return the number of possible digits.

        Returns:
            int: The number of possible digits.
        """
        return sum(self.possibles)

    def set_possible(self, digits: list[int]) -> None:
        """Set specific digits as possible, making others impossible.

        Args:
            digits (list[int]): The list of digits to mark as possible.
        """
        for digit in self.digit_range:
            if digit not in digits:
                self[digit] = False

    def set_impossible(self, digits: list[int]) -> None:
        """Set specific digits as impossible.

        Args:
            digits (list[int]): The list of digits to mark as impossible.
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
