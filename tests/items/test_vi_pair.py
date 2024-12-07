"""TestViPair."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.sum_pair import SumPair
from src.items.vi_pair import VIPair
from tests.items.test_sum_pair import TestSumPair


class TestVIPair(TestSumPair):
    """Test suite for the VIPair class."""

    def setUp(self) -> None:
        """Set up the board and VIPair item for testing."""
        super().setUp()
        # Create a VIPair item with two cells
        self.item = VIPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        # Set the size of the pair to 2
        self.size = 2

    @property
    def clazz(self):
        """Return the VIPair class."""
        return VIPair

    @property
    def config(self):
        """Return the configuration string for VIPair."""
        return "VIPair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Return whether VIPair has a rule."""
        return True

    @property
    def total(self) -> int:
        """Return the total value of VIPair."""
        return 6

    @property
    def representation(self) -> str:
        """Return the string representation of VIPair."""
        return (
            "VIPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for VIPair."""
        return {Cell, SumPair, Item, Pair, VIPair, Region, ComposedItem}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
