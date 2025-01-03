"""TestStandardRegionSet module."""

import unittest
from typing import Type

from src.board.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region_set import RegionSet
from src.items.standard_region_set import StandardRegionSet
from tests.items.test_region_sets import TestRegionSet


class TestStandardRegionSet(TestRegionSet):
    """Test suite for the StandardRegionSet class."""

    def setUp(self) -> None:
        """Set up the test environment for StandardRegionSet."""
        super().setUp()

        self.board = Board(9, 9, 3, 3)
        self.item = StandardRegionSet(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        """Return the StandardRegionSet class."""
        return StandardRegionSet

    @property
    def config(self) -> str:
        """Return the configuration string for StandardRegionSet."""
        return "StandardRegionSet:"

    @property
    def representation(self) -> str:
        """Return the string representation of StandardRegionSet."""
        return "StandardRegionSet(Board(9, 9, 3, 3, None), [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for StandardRegionSet."""
        return {Item, ComposedItem, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        """Return whether the StandardRegionSet has start rule."""
        return False


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
