"""TestRegionSets module."""

import unittest
from typing import Type

from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region_set import RegionSet
from tests.items.test_composed import TestComposed


class TestRegionSet(TestComposed):
    """Test suite for the RegionSet class."""

    def setUp(self) -> None:
        """Set up start test instance of RegionSet."""
        super().setUp()
        self.item = RegionSet(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        """Return the RegionSet class."""
        return RegionSet

    @property
    def config(self) -> str:
        """Return the configuration string for RegionSet."""
        return "RegionSet:"

    @property
    def representation(self) -> str:
        """Return the string representation of RegionSet."""
        return "RegionSet(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the RegionSet instance should belong to."""
        return {Item, ComposedItem, RegionSet}

    @property
    def has_rule(self) -> bool:
        """Return whether RegionSet has an associated rule."""
        return False


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
