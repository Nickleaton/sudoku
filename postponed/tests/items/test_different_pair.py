"""TestDifferencePair."""
import unittest
from typing import Type

from postponed.src.items.difference_pair import DifferencePair
from postponed.src.items.pair import Pair
from postponed.tests.items.test_pair import TestPair
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestDifferencePair(TestPair):
    """Test suite for the DifferencePair class."""

    def setUp(self) -> None:
        """Set up the test environment, creating the board and the DifferencePair constraint."""
        super().setUp()
        self.item = DifferencePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), [1, 2])
        self.size = 2

    @property
    def clazz(self):
        """Return the DifferencePair class."""
        return DifferencePair

    @property
    def representation(self) -> str:
        """Return the string representation of the DifferencePair constraint."""
        return (
            "DifferencePair"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3), "
            "[1, 2]"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the DifferencePair."""
        return "DifferencePair: 12-13=1,2"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the DifferencePair should belong to."""
        return {Cell, Item, Pair, DifferencePair, ComposedItem, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
