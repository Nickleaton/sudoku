"""TestXPair."""

import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.sum_pair import SumPair
from src.items.x_pair import XPair
from tests.items.test_variable_sum_pair import TestSumPair


class TestXPair(TestSumPair):
    """Test suite for the XPair class."""

    def setUp(self) -> None:
        """Set up the board and XPair item for testing."""
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
        """Return whether XPair has a rule."""
        return True

    @property
    def total(self) -> int:
        """Return the total value for the XPair."""
        return 10

    @property
    def representation(self) -> str:
        """Return the string representation of the XPair."""
        return (
            "XPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for XPair."""
        return {Cell, SumPair, Item, Pair, XPair, Region, ComposedItem}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
