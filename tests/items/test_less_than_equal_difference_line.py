"""TestLessThanEqualDifferenceLine."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.less_than_equal_difference_line import LessThanEqualDifferenceLine
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_line import TestLine


class TestLessThanEqualDifferenceLine(TestLine):
    """Test suite for the LessThanEqualDifferenceLine class, inheriting from TestLine."""

    def setUp(self) -> None:
        """Set up the test case, initializing the size for the composed list."""
        super().setUp()
        # Line is length 3
        # Size is 3 + 2 difference pairs = 5 vectors in the composed list
        self.size = 5

    @property
    def clazz(self):
        """Return the LessThanEqualDifferenceLine class."""
        return LessThanEqualDifferenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for LessThanEqualDifferenceLine."""
        return "LessThanEqualDifferenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the LessThanEqualDifferenceLine instance has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the LessThanEqualDifferenceLine instance should belong to."""
        return {
            Cell,
            ComposedItem,
            DifferencePair,
            Item,
            LessThanEqualDifferenceLine,
            LessThanEqualDifferencePair,
            Line,
            Pair,
            Region
        }


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
