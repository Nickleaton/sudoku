"""TestSumPair module."""

import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.sum_pair import SumPair
from tests.items.test_pair import TestPair


class TestSumPair(TestPair):
    """Test case for SumPair class."""

    def setUp(self) -> None:
        """Set up the test environment for SumPair."""
        super().setUp()
        self.item = SumPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the SumPair class."""
        return SumPair

    @property
    def representation(self) -> str:
        """Return the string representation of SumPair."""
        return (
            "SumPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for SumPair."""
        return "SumPair: 12-13"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for SumPair."""
        return {Cell, Item, Pair, SumPair, ComposedItem, Region}

    @property
    def inside(self) -> Cell:
        """Return the 'inside' cell of SumPair."""
        return Cell.make(self.board, 1, 2)

    @property
    def has_rule(self) -> bool:
        """Return whether SumPair has a rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
