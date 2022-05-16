import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.palindrome import Palindrome
from src.items.region import Region
from tests.items.test_line import TestLine


class TestPalindrome(TestLine):

    @property
    def clazz(self):
        return Palindrome

    @property
    def config(self) -> str:
        return "Palindrome: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Palindrome, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
