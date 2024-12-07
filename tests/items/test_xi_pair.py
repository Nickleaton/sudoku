"""TestXiPair."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.sum_pair import SumPair
from src.items.xi_pair import XIPair
from tests.items.test_variable_sum_pair import TestSumPair


class TestXIPair(TestSumPair):
    """Test suite for the XIPair class."""

    def setUp(self) -> None:
        """Set up the board and XIPair item for testing."""
        super().setUp()
        self.item = XIPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the XIPair class."""
        return XIPair

    @property
    def config(self):
        """Return the configuration string for XIPair."""
        return "XIPair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Return whether XIPair has a rule."""
        return True

    @property
    def total(self) -> int:
        """Return the total value for the XIPair."""
        return 11

    @property
    def representation(self) -> str:
        """Return the string representation of the XIPair."""
        return (
            "XIPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for XIPair."""
        return {Cell, SumPair, Item, Pair, XIPair, ComposedItem, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
