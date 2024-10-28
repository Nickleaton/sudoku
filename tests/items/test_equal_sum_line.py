import unittest
from typing import Type

from src.items.equal_sum_line import EqualSumLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestEqualSum(TestLine):

    @property
    def clazz(self):
        return EqualSumLine

    @property
    def config(self) -> str:
        return "EqualSumLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {EqualSumLine, Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()