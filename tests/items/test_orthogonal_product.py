"""TestOrthogonalProduct."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.orthogonal_product import OrthogonalProduct
from src.items.product import Product
from src.items.region import Region
from src.utils.coord import Coord
from tests.items.test_product import TestProduct


class TestOrthogonalProduct(TestProduct):
    """Test suite for the OrthogonalProduct class."""

    def setUp(self) -> None:
        """Set up the test environment for OrthogonalProduct."""
        super().setUp()
        self.item = OrthogonalProduct(self.board, Coord(2, 2), 5)
        self.size = 4

    @property
    def clazz(self):
        """Return the OrthogonalProduct class."""
        return OrthogonalProduct

    @property
    def representation(self) -> str:
        """Return the string representation of the OrthogonalProduct instance."""
        return "OrthogonalProduct(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), 5)"

    @property
    def config(self) -> str:
        """Return the configuration string for OrthogonalProduct."""
        return "OrthogonalProduct: 22=5"

    @property
    def has_rule(self) -> bool:
        """Return whether the OrthogonalProduct instance has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the OrthogonalProduct instance should belong to."""
        return {Cell, ComposedItem, Item, OrthogonalProduct, Product, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
