"""TestColumns."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.column import Column
from src.items.columns import Columns
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.region_set import RegionSet
from src.items.standard_region import StandardRegion
from src.items.standard_region_set import StandardRegionSet
from tests.items.test_rows import TestStandardRegionSet


class TestColumns(TestStandardRegionSet):
    """Test suite for the Columns item in the Board."""

    def setUp(self) -> None:
        """Set up the Board and Columns instance for testing."""
        super().setUp()
        self.item = Columns(self.board)
        self.size = 9

    @property
    def clazz(self):
        """Return the Columns class."""
        return Columns

    @property
    def config(self) -> str:
        """Return the configuration string for the Columns item."""
        return "Columns:"

    @property
    def representation(self) -> str:
        """Return the string representation for the Columns item."""
        return "Columns(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Columns item should belong to."""
        return {Item, ComposedItem, Cell, StandardRegion, Region, Column, Columns, StandardRegion, RegionSet,
                StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        """Indicates if the Columns item has a rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
