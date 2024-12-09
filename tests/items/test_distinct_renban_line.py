"""TestDistinctRenbanLine."""
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
    """Test suite for the DistinctRenbanLine class."""

    @property
    def clazz(self):
        """Return the DistinctRenbanLine class."""
        return DistinctRenbanLine

    @property
    def config(self) -> str:
        """Return the configuration string for the DistinctRenbanLine."""
        return "DistinctRenbanLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the DistinctRenbanLine has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the DistinctRenbanLine should belong to."""
        return {Cell, ComposedItem, Item, Line, Region, RenbanLine, DistinctRenbanLine}

    def test_digit_str(self):
        """Test the conversion of digits to strings."""
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
        """Test the calculation of powers for the DistinctRenbanLine."""
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
        """Test the conversion of power value_list to string representations."""
        self.assertEqual('1', DistinctRenbanLine.power_str(1))
        self.assertEqual('2', DistinctRenbanLine.power_str(2))
        self.assertEqual('9', DistinctRenbanLine.power_str(256))
        self.assertEqual('9', DistinctRenbanLine.power_str(256))
        self.assertEqual('123', DistinctRenbanLine.power_str(1 + 2 + 4))
        self.assertEqual('789', DistinctRenbanLine.power_str(64 + 128 + 256))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
