import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.distinct_renban import DistinctRenban
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.renban import Renban
from tests.items.test_renban import TestRenban


class TestDistinctRenban(TestRenban):

    @property
    def clazz(self):
        return DistinctRenban

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region, Renban, DistinctRenban}

    def test_digit_str(self):
        self.assertEqual(1, DistinctRenban.digits_to_str([1]))
        self.assertEqual(2, DistinctRenban.digits_to_str([2]))
        self.assertEqual(4, DistinctRenban.digits_to_str([3]))
        self.assertEqual(8, DistinctRenban.digits_to_str([4]))
        self.assertEqual(16, DistinctRenban.digits_to_str([5]))
        self.assertEqual(32, DistinctRenban.digits_to_str([6]))
        self.assertEqual(64, DistinctRenban.digits_to_str([7]))
        self.assertEqual(128, DistinctRenban.digits_to_str([8]))
        self.assertEqual(256, DistinctRenban.digits_to_str([9]))

        self.assertEqual(1 + 2 + 4, DistinctRenban.digits_to_str([1, 2, 3]))
        self.assertEqual(64 + 128 + 256, DistinctRenban.digits_to_str([7, 8, 9]))

    def test_power(self):
        self.assertEqual(1, DistinctRenban.power(1))
        self.assertEqual(2, DistinctRenban.power(2))
        self.assertEqual(4, DistinctRenban.power(3))
        self.assertEqual(8, DistinctRenban.power(4))
        self.assertEqual(16, DistinctRenban.power(5))
        self.assertEqual(32, DistinctRenban.power(6))
        self.assertEqual(64, DistinctRenban.power(7))
        self.assertEqual(128, DistinctRenban.power(8))
        self.assertEqual(256, DistinctRenban.power(9))

    def test_power_string(self):
        self.assertEqual('1', DistinctRenban.power_str(1))
        self.assertEqual('2', DistinctRenban.power_str(2))
        self.assertEqual('9', DistinctRenban.power_str(256))
        self.assertEqual('9', DistinctRenban.power_str(256))
        self.assertEqual('123', DistinctRenban.power_str(1+2+4))
        self.assertEqual('789', DistinctRenban.power_str(64 + 128 + 256))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
