"""TestLessThanEqualDifferenceLine."""
import unittest
from typing import Type

from postponed.src.items.difference_pair import DifferencePair
from postponed.src.items.le_difference_line import LEDifferenceLine
from postponed.src.items.le_difference_pair import LEDifferencePair
from postponed.src.items.line import Line
from postponed.src.items.pair import Pair
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestLEDifferenceLine(TestLine):
    """Test suite for the LEDifferenceLine class, inheriting from TestLine."""

    def setUp(self) -> None:
        """Set up the test case, initializing the size for the composed list."""
        super().setUp()
        # Line is length 3
        # Size is 3 + 2 difference pairs = 5 vectors in the composed list
        self.size = 5

    @property
    def clazz(self):
        """Return the LEDifferenceLine class."""
        return LessThanEqualDifferenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for LEDifferenceLine."""
        return "LEDifferenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the LEDifferenceLine instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the LEDifferenceLine instance should belong to."""
        return {
            Cell,
            ComposedItem,
            DifferencePair,
            Item,
            LEDifferenceLine,
            LEDifferencePair,
            Line,
            Pair,
            Region
        }


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
