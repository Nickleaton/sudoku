"""TestFrameProduct."""
import unittest
from typing import Type

from postponed.src.items.first_n import FirstN
from postponed.src.items.frame_product import FrameProduct
from postponed.tests.items.test_first_n import TestFirstN
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side


class TestFrameProduct(TestFirstN):
    """Test suite for the FrameProduct class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the FrameProduct constraint."""
        super().setUp()
        self.item = FrameProduct(self.board, Side.top, 1, 20)
        self.size = 3

    @property
    def clazz(self):
        """Return the FrameProduct class."""
        return FrameProduct

    @property
    def representation(self) -> str:
        """Return start_location string representation of the FrameProduct instance."""
        return "FrameProduct(Board(9, 9, {}), Side.top, 20)"

    @property
    def config(self) -> str:
        """Return the configuration string for the FrameProduct."""
        return "FrameProduct: T1=20"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the FrameProduct."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FrameProduct should belong to."""
        return {Cell, ComposedItem, FirstN, FrameProduct, Item, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
