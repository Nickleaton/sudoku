"""TestColumn."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.column import Column
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestColumn(TestStandardRegion):
    """Test suite for the Column constraint in the Board."""

    def setUp(self) -> None:
        """Set up the Board and Column instance for testing."""
        super().setUp()
        self.item = Column(self.board, 1)
        self.size = 9

    @property
    def clazz(self):
        """Return the Column class."""
        return Column

    @property
    def config(self) -> str:
        """Return the configuration string for the Column constraint."""
        return "Column: 1"

    @property
    def representation(self) -> str:
        """Return the string representation for the Column constraint."""
        return "Column(Board(Coord(9, 9), Digits(1, 9), Tags({})), 1)"

    @property
    def has_rule(self) -> bool:
        """Indicates if the Column has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Column constraint should belong to."""
        return {Item, ComposedItem, Cell, Region, StandardRegion, Column}

    def test_in(self):
        """Test if start_location Cell is contained within the Column."""
        self.assertIn(Cell.make(self.board, 2, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
