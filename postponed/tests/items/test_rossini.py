"""TestRossini module."""

import unittest
from typing import Type

from postponed.src.items.first_n import FirstN
from postponed.src.items.rossini import Rossini
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.utils.order import Order
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestRossini(TestRegion):
    """Test suite for the Rossini class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.item = Rossini(self.board, Side.top, 1, Order.increasing)
        self.size = 3

    @property
    def clazz(self):
        """Return the Rossini class."""
        return Rossini

    @property
    def representation(self) -> str:
        """Return the string representation of the Rossini instance."""
        return "Rossini(Board(9, 9, {}), Side.top, 1, Order.increasing)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes the Rossini instance should belong to."""
        return {Cell, ComposedItem, FirstN, Item, Region, Rossini}

    @property
    def config(self) -> str:
        """Return the configuration string for the Rossini instance."""
        return "Rossini: T1=I"

    @property
    def has_rule(self) -> bool:
        """Return whether the Rossini instance has an associated rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
