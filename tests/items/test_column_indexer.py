"""TestColumnIndexer."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.column_indexer import ColumnIndexer
from src.items.composed_item import ComposedItem
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_indexer import TestIndexer


class TestColumnIndexer(TestIndexer):
    """Test suite for the ColumnIndexer constraint in the Board."""

    def setUp(self) -> None:
        """Set up the Board and ColumnIndexer instance for testing."""
        super().setUp()

        self.item = ColumnIndexer(self.board, 1)
        self.size = 9

    @property
    def clazz(self):
        """Return the ColumnIndexer class."""
        return ColumnIndexer

    @property
    def representation(self) -> str:
        """Return the string representation for the ColumnIndexer constraint."""
        return "ColumnIndexer(Board(9, 9, 3, 3, None), 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the ColumnIndexer constraint should belong to."""
        return {Cell, ColumnIndexer, ComposedItem, Indexer, Item, Region, StandardRegion}

    @property
    def config(self) -> str:
        """Return the configuration string for the ColumnIndexer constraint."""
        return "ColumnIndexer: 1"

    @property
    def has_rule(self) -> bool:
        """Indicates if the ColumnIndexer has start rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
