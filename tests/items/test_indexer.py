"""TestIndexer."""
import unittest
from typing import Type

from src.items.composed_item import ComposedItem
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestIndexer(TestStandardRegion):
    """Test suite for the Indexer class."""

    def setUp(self) -> None:
        """Set up the test case with start board and an instance of Indexer."""
        super().setUp()

        self.item = Indexer(self.board, 1)
        self.size = 0

    @property
    def clazz(self):
        """Return the Indexer class."""
        return Indexer

    @property
    def representation(self) -> str:
        """Return start string representation of the Indexer instance."""
        return "Indexer(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Indexer should belong to."""
        return {Item, ComposedItem, StandardRegion, Region, Indexer}

    @property
    def config(self) -> str:
        """Return the configuration string for Indexer."""
        return "Indexer: 1"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for Indexer."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
