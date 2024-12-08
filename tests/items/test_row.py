"""TestRow module."""

import unittest
from typing import Type

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.row import Row
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestRow(TestStandardRegion):
    """Test suite for the Row class."""

    def setUp(self) -> None:
        """Set up the test environment for Row."""
        super().setUp()

        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Row(self.board, 1)
        self.size = 9

    @property
    def clazz(self):
        """Return the Row class."""
        return Row

    @property
    def config(self) -> str:
        """Return the configuration string for the Row instance."""
        return "Row: 1"

    @property
    def representation(self) -> str:
        """Return the string representation of the Row instance."""
        return "Row(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        """Return whether the Row instance has an associated rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes the Row instance should belong to."""
        return {Item, ComposedItem, Cell, Region, StandardRegion, Row}

    def test_in(self):
        """Test if specific cells are in or out of the Row instance."""
        self.assertIn(Cell.make(self.board, 1, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
