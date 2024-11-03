from typing import List

from typing_extensions import Self


class BookKeeping:

    def __init__(self, maximum_digit: int):
        self.maximum_digit = maximum_digit
        self.digit_range = range(1, maximum_digit + 1)
        self.possibles = [True] * self.maximum_digit

    def __getitem__(self, digit: int) -> bool:
        return self.possibles[digit - 1]

    def __setitem__(self, digit: int, value: bool) -> None:
        self.possibles[digit - 1] = value

    def __and__(self, other) -> 'BookKeeping':
        assert isinstance(other, BookKeeping)
        assert self.maximum_digit == other.maximum_digit
        result = BookKeeping(self.maximum_digit)
        for i in self.digit_range:
            result[i] = self[i] and other[i]
        return result

    def __or__(self, other) -> 'BookKeeping':
        assert isinstance(other, BookKeeping)
        assert self.maximum_digit == other.maximum_digit
        result = BookKeeping(self.maximum_digit)
        for i in self.digit_range:
            result[i] = self[i] or other[i]
        return result

    def __invert__(self) -> 'BookKeeping':
        result = BookKeeping(self.maximum_digit)
        for i in self.digit_range:
            result[i] = not self[i]
        return result

    def __eq__(self, other) -> bool:
        assert isinstance(other, BookKeeping)
        assert self.maximum_digit == other.maximum_digit
        for i in self.digit_range:
            if self[i] != other[i]:
                return False
        return True

    def __str__(self) -> str:
        return "".join([str(i) if self[i] else ' ' for i in self.digit_range])

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.maximum_digit)})"

    def set_possible(self, digits: List[int]) -> None:
        for digit in self.digit_range:
            if digit not in digits:
                self[digit] = False

    def set_impossible(self, digits: List[int]) -> None:
        for digit in self.digit_range:
            if digit in digits:
                self[digit] = False

    def set_odd(self) -> None:
        for digit in self.digit_range:
            if digit % 2 != 1:
                self[digit] = False

    def set_even(self) -> None:
        for digit in self.digit_range:
            if digit % 2 != 0:
                self[digit] = False

    def set_minimum(self, lower: int) -> None:
        for digit in self.digit_range:
            if digit < lower:
                self[digit] = False

    def set_maximum(self, upper: int) -> None:
        for digit in self.digit_range:
            if digit > upper:
                self[digit] = False

    def set_range(self, lower: int, upper: int) -> None:
        self.set_minimum(lower)
        self.set_maximum(upper)

    def fixed(self) -> bool:
        return sum(self.possibles) == 1

    def is_possible(self, digit: int) -> bool:
        return self[digit]

    def is_unique(self) -> bool:
        return sum(self.possibles) == 1