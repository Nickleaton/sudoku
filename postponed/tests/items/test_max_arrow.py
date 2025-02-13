"""TestMaxArrow."""
import unittest
from typing import Type

from postponed.src.items.line import Line
from postponed.src.items.max_arrow import MaxArrowLine
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestMaxArrow(TestLine):
    """Test suite for the MaxArrowLine class."""

    @property
    def clazz(self):
        """Return the MaxArrowLine class."""
        return MaxArrowLine

    @property
    def config(self) -> str:
        """Return the configuration string for the MaxArrowLine instance."""
        return "MaxArrowLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the MaxArrowLine instance has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the MaxArrowLine instance should belong to."""
        return {MaxArrowLine, Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
