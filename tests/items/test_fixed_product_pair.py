"""TestFixedProductPair."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.fixed_pair import FixedPair
from src.items.fixed_product_pair import FixedProductPair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_fixed_pair import TestFixedPair


class TestFixedProductPair(TestFixedPair):
    """Test suite for the FixedProductPair class."""

    def setUp(self) -> None:
        """Set up the test environment by creating a board and initializing the FixedProductPair item."""
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FixedProductPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), 1)
        self.size = 2

    @property
    def clazz(self):
        """Return the FixedProductPair class."""
        from src.items.fixed_product_pair import FixedProductPair
        return FixedProductPair

    @property
    def representation(self) -> str:
        """Return a string representation of the FixedProductPair instance."""
        return (
            "FixedProductPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "1"
            ")"
        )

    @property
    def config(self) -> str:
        """Return the configuration string for the FixedProductPair."""
        return "FixedProductPair: 12-13=1"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the FixedProductPair should belong to."""
        return {Cell, Item, Pair, FixedPair, FixedProductPair, ComposedItem, Region}

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the FixedProductPair."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
