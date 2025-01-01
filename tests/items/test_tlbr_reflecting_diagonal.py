"""TestTLBRReflecting module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.tlbr_reflecting_diagonal import TLBRReflecting
from tests.items.test_diagonal import TestDiagonal


class TestTLBRReflecting(TestDiagonal):
    """Test case for TLBRReflecting class, which extends Diagonal."""

    def setUp(self) -> None:
        """Set up the test case with start Board and TLBRReflecting constraint."""
        super().setUp()

        self.item = TLBRReflecting(self.board)
        self.size = 9

    @property
    def clazz(self):
        """Return the TLBRReflecting class."""
        return TLBRReflecting

    @property
    def has_rule(self) -> bool:
        """Return True indicating that the TLBRReflecting constraint has start rule."""
        return True

    @property
    def representation(self) -> str:
        """Return the string representation of the TLBRReflecting constraint."""
        return "TLBRReflecting(Board(9, 9, 3, 3, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for TLBRReflecting."""
        return {Item, Cell, ComposedItem, Region, Diagonal, TLBRReflecting}

    @property
    def config(self) -> str:
        """Return the configuration string for TLBRReflecting."""
        return "TLBRReflecting:"

    def test_in(self):
        """Test that specific cells are part of the TLBRReflecting region."""
        self.assertIn(Cell.make(self.board, 1, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
