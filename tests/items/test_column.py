"""TestColumn."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.column import Column
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestColumn(TestStandardRegion):
    """Test suite for the Column item in the Board."""

    def setUp(self) -> None:
        """Set up the Board and Column instance for testing."""
        super().setUp()

        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Column(self.board, 1)
        self.size = 9

    @property
    def clazz(self):
        """Return the Column class."""
        return Column

    @property
    def config(self) -> str:
        """Return the configuration string for the Column item."""
        return "Column: 1"

    @property
    def representation(self) -> str:
        """Return the string representation for the Column item."""
        return "Column(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        """Indicates if the Column has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Column item should belong to."""
        return {Item, ComposedItem, Cell, Region, StandardRegion, Column}

    def test_in(self):
        """Test if a Cell is contained within the Column."""
        self.assertIn(Cell.make(self.board, 2, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
