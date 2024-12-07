"""TestRowIndexer module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.row_indexer import RowIndexer
from src.items.standard_region import StandardRegion
from tests.items.test_indexer import TestIndexer


class TestRowIndexer(TestIndexer):
    """Test suite for the RowIndexer class."""

    def setUp(self) -> None:
        """Set up the test environment for RowIndexer."""
        super().setUp()

        self.item = RowIndexer(self.board, 1)
        self.size = 9

    @property
    def clazz(self):
        """Return the RowIndexer class."""
        return RowIndexer

    @property
    def representation(self) -> str:
        """Return the string representation of the RowIndexer instance."""
        return "RowIndexer(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes the RowIndexer instance should belong to."""
        return {Cell, RowIndexer, ComposedItem, Indexer, Item, Region, StandardRegion}

    @property
    def config(self) -> str:
        """Return the configuration string for the RowIndexer instance."""
        return "RowIndexer: 1"

    @property
    def has_rule(self) -> bool:
        """Return whether the RowIndexer instance has an associated rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
