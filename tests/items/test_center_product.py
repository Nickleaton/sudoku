"""TestCenterProduct."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.center_product import CenterProduct
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.product import Product
from src.items.region import Region
from src.utils.coord import Coord
from tests.items.test_orthogonal_product import TestProduct


class TestCenterProduct(TestProduct):
    """Test suite for the CenterProduct item in the Board."""

    def setUp(self) -> None:
        """Set up the Board and CenterProduct instance for testing."""
        super().setUp()
        self.item = CenterProduct(self.board, Coord(2, 2), 5)
        self.size = 4

    @property
    def clazz(self):
        """Return the CenterProduct class."""
        return CenterProduct

    @property
    def representation(self) -> str:
        """Return the string representation for the CenterProduct item."""
        return "CenterProduct(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), 5)"

    @property
    def config(self) -> str:
        """Return the configuration string for the CenterProduct item."""
        return "CenterProduct: 22=5"

    @property
    def has_rule(self) -> bool:
        """Indicates if the CenterProduct has a rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the CenterProduct item should belong to."""
        return {Cell, CenterProduct, ComposedItem, Item, Product, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
