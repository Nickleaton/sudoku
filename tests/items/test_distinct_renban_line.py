import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.distinct_renban_line import DistinctRenbanLine
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.renban_line import RenbanLine
from tests.items.test_renban_line import TestRenbanLine


class TestDistinctRenbanLine(TestRenbanLine):

    @property
    def clazz(self):
        return DistinctRenbanLine

    @property
    def config(self) -> str:
        return "DistinctRenbanLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, Item, Line, Region, RenbanLine, DistinctRenbanLine}

    def test_digit_str(self):
        self.assertEqual(1, DistinctRenbanLine.digits_to_str([1]))
        self.assertEqual(2, DistinctRenbanLine.digits_to_str([2]))
        self.assertEqual(4, DistinctRenbanLine.digits_to_str([3]))
        self.assertEqual(8, DistinctRenbanLine.digits_to_str([4]))
        self.assertEqual(16, DistinctRenbanLine.digits_to_str([5]))
        self.assertEqual(32, DistinctRenbanLine.digits_to_str([6]))
        self.assertEqual(64, DistinctRenbanLine.digits_to_str([7]))
        self.assertEqual(128, DistinctRenbanLine.digits_to_str([8]))
        self.assertEqual(256, DistinctRenbanLine.digits_to_str([9]))

        self.assertEqual(1 + 2 + 4, DistinctRenbanLine.digits_to_str([1, 2, 3]))
        self.assertEqual(64 + 128 + 256, DistinctRenbanLine.digits_to_str([7, 8, 9]))

    def test_power(self):
        self.assertEqual(1, DistinctRenbanLine.power(1))
        self.assertEqual(2, DistinctRenbanLine.power(2))
        self.assertEqual(4, DistinctRenbanLine.power(3))
        self.assertEqual(8, DistinctRenbanLine.power(4))
        self.assertEqual(16, DistinctRenbanLine.power(5))
        self.assertEqual(32, DistinctRenbanLine.power(6))
        self.assertEqual(64, DistinctRenbanLine.power(7))
        self.assertEqual(128, DistinctRenbanLine.power(8))
        self.assertEqual(256, DistinctRenbanLine.power(9))

    def test_power_string(self):
        self.assertEqual('1', DistinctRenbanLine.power_str(1))
        self.assertEqual('2', DistinctRenbanLine.power_str(2))
        self.assertEqual('9', DistinctRenbanLine.power_str(256))
        self.assertEqual('9', DistinctRenbanLine.power_str(256))
        self.assertEqual('123', DistinctRenbanLine.power_str(1 + 2 + 4))
        self.assertEqual('789', DistinctRenbanLine.power_str(64 + 128 + 256))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
