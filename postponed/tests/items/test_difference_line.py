"""TestDifferenceLine."""
import unittest
from typing import Type

from postponed.src.items.difference_line import DifferenceLine
from postponed.src.items.line import Line
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestDifferenceLine(TestLine):
    """Test suite for the DifferenceLine class."""

    @property
    def clazz(self):
        """Return the DifferenceLine class."""
        return DifferenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for the DifferenceLine."""
        return "DifferenceLine: 11, 12, 13"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the DifferenceLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
