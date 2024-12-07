"""TestSpecialRegion module."""

import unittest
from typing import Type

from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.special_region import SpecialRegion
from tests.items.test_region import TestRegion


class TestSpecialRegion(TestRegion):
    """Test suite for the SpecialRegion class."""

    def setUp(self) -> None:
        """Set up the test environment for SpecialRegion."""
        super().setUp()
        self.item = SpecialRegion(self.board)
        self.size = 0

    @property
    def clazz(self):
        """Return the SpecialRegion class."""
        return SpecialRegion

    @property
    def config(self) -> str:
        """Return the configuration string for the SpecialRegion."""
        return "SpecialRegion:"

    @property
    def representation(self) -> str:
        """Return the string representation of the SpecialRegion."""
        return "SpecialRegion(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def has_rule(self) -> bool:
        """Return whether the SpecialRegion has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for the SpecialRegion."""
        return {Item, ComposedItem, Region, SpecialRegion}

    def test_in(self):
        """Test the 'in' operator for the SpecialRegion."""
        self.assertListEqual([], self.item.cells)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
