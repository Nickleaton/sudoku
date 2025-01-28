"""TestEqualSumLine."""
import unittest
from typing import Type

from postponed.src.items.equal_sum_line import EqualSumLine
from postponed.src.items.line import Line
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestEqualSum(TestLine):
    """Test suite for the EqualSumLine class."""

    @property
    def clazz(self):
        """Return the EqualSumLine class."""
        return EqualSumLine

    @property
    def config(self) -> str:
        """Return the configuration string for the EqualSumLine."""
        return "EqualSumLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the EqualSumLine has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the EqualSumLine should belong to."""
        return {EqualSumLine, Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
