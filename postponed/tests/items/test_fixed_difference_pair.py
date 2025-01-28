"""TestFixedDifferencePair."""
import unittest
from typing import Type

from postponed.src.items.fixed_difference_pair import FixedDifferencePair
from postponed.src.items.fixed_pair import FixedPair
from postponed.src.items.pair import Pair
from postponed.tests.items.test_fixed_pair import TestFixedPair
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestFixedDifferencePair(TestFixedPair):
    """Test suite for the FixedDifferencePair class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the FixedDifferencePair constraint."""
        super().setUp()
        self.item = FixedDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            1
        )
        self.size = 2

    @property
    def clazz(self):
        """Return the FixedDifferencePair class."""
        return FixedDifferencePair

    @property
    def representation(self) -> str:
        """Return start_location string representation of the FixedDifferencePair instance."""
        return (
            "FixedDifferencePair"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3), "
            "1"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FixedDifferencePair."""
        return "FixedDifferencePair: 12-13=1"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FixedDifferencePair should belong to."""
        return {Cell, Item, Pair, FixedPair, FixedDifferencePair, ComposedItem, Region}

    @property
    def has_rule(self) -> bool:
        """Return True if the FixedDifferencePair has start_location rule, otherwise False."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
