"""TestVPair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from postponed.src.items.pair import Pair
from src.items.region import Region
from postponed.src.items.sum_pair import SumPair
from postponed.src.items.v_pair import VPair
from postponed.tests.items.test_variable_sum_pair import TestSumPair


class TestVPair(TestSumPair):
    """Test suite for the VPair class."""

    def setUp(self) -> None:
        """Set up the board and VPair constraint for testing."""
        super().setUp()
        self.item = VPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the VPair class."""
        return VPair

    @property
    def config(self):
        """Return the configuration string for VPair."""
        return "VPair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Return whether the rule applies for VPair."""
        return True

    @property
    def total(self) -> int:
        """Return the total number for VPair."""
        return 5

    @property
    def representation(self) -> str:
        """Return the string representation of VPair."""
        return (
            "VPair"
            "("
            "Board(9, 9, {}), "
            "Cell(Board(9, 9, {}), 1, 2), "
            "Cell(Board(9, 9, {}), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for VPair."""
        return {Cell, SumPair, Item, Pair, VPair, Region, ComposedItem}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
