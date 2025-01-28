"""TestGEDifferenceLine."""
import unittest
from typing import Type

from postponed.src.items.difference_line import DifferenceLine
from postponed.src.items.fixed_difference_pair import FixedDifferencePair
from postponed.src.items.fixed_pair import FixedPair
from postponed.src.items.ge_difference_line import GEDifferenceLine
from postponed.src.items.ge_difference_pair import GEDifferencePair
from postponed.src.items.line import Line
from postponed.src.items.pair import Pair
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestGEDifferenceLine(TestLine):
    """Test suite for the GEDifferenceLine class."""

    def setUp(self) -> None:
        """Set up the test case with start_location board and an instance of GEDifferenceLine."""
        super().setUp()
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = GEDifferenceLine(self.board, cells, 5)
        self.size = 5

    @property
    def clazz(self):
        """Return the GEDifferenceLine class."""
        return GEDifferenceLine

    @property
    def config(self) -> str:
        """Return the configuration string for GEDifferenceLine."""
        return "GEDifferenceLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for GEDifferenceLine."""
        return True

    @property
    def representation(self) -> str:
        """Return start_location string representation of the GEDifferenceLine instance."""
        return (
            "GEDifferenceLine"
            "("
            "Board(9, 9, {}), "
            "["
            "Cell(Board(9, 9, {}), 1, 1), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3)"
            "], "
            "5"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the GEDifferenceLine should belong to."""
        return {Cell, ComposedItem, DifferenceLine, FixedDifferencePair, FixedPair, GEDifferenceLine,
                GEDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
