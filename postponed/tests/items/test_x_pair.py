"""TestXPair."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from postponed.src.items.pair import Pair
from src.items.region import Region
from postponed.src.items.sum_pair import SumPair
from postponed.src.items.x_pair import XPair
from postponed.tests.items.test_variable_sum_pair import TestSumPair


class TestXPair(TestSumPair):
    """Test suite for the XPair class."""

    def setUp(self) -> None:
        """Set up the board and XPair constraint for testing."""
        super().setUp()
        self.item = XPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the XPair class."""
        return XPair

    @property
    def config(self):
        """Return the configuration string for XPair."""
        return "XPair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Return whether XPair has start_location rule."""
        return True

    @property
    def total(self) -> int:
        """Return the total number for the XPair."""
        return 10

    @property
    def representation(self) -> str:
        """Return the string representation of the XPair."""
        return (
            "XPair"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for XPair."""
        return {Cell, SumPair, Item, Pair, XPair, Region, ComposedItem}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
