"""TestGreaterThanEqualDifferencePair."""
import unittest
from typing import Type

from postponed.src.items.fixed_difference_pair import FixedDifferencePair
from postponed.src.items.fixed_pair import FixedPair
from postponed.src.items.ge_difference_pair import GEDifferencePair
from postponed.src.items.pair import Pair
from postponed.tests.items.test_different_pair import TestDifferencePair
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestGEDifferencePair(TestDifferencePair):
    """Test suite for the GEDifferencePair class."""

    def setUp(self) -> None:
        """Set up the test case with start_location board and an instance of GEDifferencePair."""
        super().setUp()
        self.item = GEDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            1
        )
        self.size = 2

    @property
    def clazz(self):
        """Return the GEDifferencePair class."""
        return GEDifferencePair

    @property
    def config(self) -> str:
        """Return the configuration string for GEDifferencePair."""
        return "GEDifferencePair: 12-13=1"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for GEDifferencePair."""
        return True

    @property
    def difference(self) -> int:
        """Return the difference number for the GEDifferencePair."""
        return 1

    @property
    def representation(self) -> str:
        """Return start_location string representation of the GEDifferencePair instance."""
        return (
            "GEDifferencePair"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3), "
            "1"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GEDifferencePair should belong to."""
        return {Cell, FixedDifferencePair, FixedPair, Item, Pair, GEDifferencePair, ComposedItem, Region}

    def test_difference(self):
        """Test that the difference is correctly calculated."""
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
