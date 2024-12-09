"""TestTLBR module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.standard_diagonal import StandardDiagonal
from src.items.tlbr import TLBR
from tests.items.test_standard_diagonal import TestStandardDiagonal


class TestTLBR(TestStandardDiagonal):
    """Test case for TLBR class, which extends StandardDiagonal."""

    def setUp(self) -> None:
        """Set up the test case with start Board and TLBR constraint."""
        super().setUp()

        self.item = TLBR(self.board)
        self.size = 9

    @property
    def clazz(self):
        """Return the TLBR class."""
        return TLBR

    @property
    def representation(self) -> str:
        """Return the string representation of the TLBR constraint."""
        return "TLBR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for TLBR."""
        return {Item, ComposedItem, Cell, Region, Diagonal, StandardDiagonal, TLBR}

    @property
    def config(self) -> str:
        """Return the configuration string for TLBR."""
        return "TLBR:"

    def test_in(self):
        """Test that specific cells are part of the TLBR region."""
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
