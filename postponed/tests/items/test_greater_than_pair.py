"""TestGreaterThanPair."""
import unittest
from typing import Type

from postponed.src.items.greater_than_pair import GreaterThanPair
from postponed.src.items.pair import Pair
from postponed.tests.items.test_pair import TestPair
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestGreaterThanPair(TestPair):
    """Test suite for the GreaterThanPair class."""

    def setUp(self) -> None:
        """Set up the test case with start_location board and an instance of GreaterThanPair."""
        super().setUp()
        self.item = GreaterThanPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the GreaterThanPair class."""
        return GreaterThanPair

    @property
    def config(self):
        """Return the configuration string for GreaterThanPair."""
        return "GreaterThanPair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for GreaterThanPair."""
        return True

    @property
    def representation(self) -> str:
        """Return start_location string representation of the GreaterThanPair instance."""
        return (
            "GreaterThanPair("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GreaterThanPair should belong to."""
        return {Cell, GreaterThanPair, Item, Pair, ComposedItem, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
