"""TestDisjointGroup."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.disjoint_group import DisjointGroup
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestDisjointGroup(TestStandardRegion):
    """Test suite for the DisjointGroup class."""

    def setUp(self) -> None:
        """Set up the test environment, creating the board and the DisjointGroup item."""
        super().setUp()
        self.item = DisjointGroup(self.board, 1)
        self.size = 9

    @property
    def clazz(self):
        """Return the DisjointGroup class."""
        return DisjointGroup

    @property
    def config(self) -> str:
        """Return the configuration string for the DisjointGroup."""
        return "DisjointGroup: 1"

    @property
    def representation(self) -> str:
        """Return the string representation of the DisjointGroup item."""
        return "DisjointGroup(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        """Return whether the DisjointGroup has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the DisjointGroup should belong to."""
        return {Item, ComposedItem, Cell, Region, StandardRegion, DisjointGroup}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
