import unittest
from typing import Type

from src.items.board import Board
from src.items.item import Item
from src.items.product import Product
from src.utils.coord import Coord
from tests.items.test_region import TestRegion


class TestProduct(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Product(self.board, Coord(2, 2), 5)

    @property
    def clazz(self):
        return Product

    @property
    def representation(self) -> str:
        return "Product(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), 5)"

    @property
    def config(self) -> str:
        return "Product: 22=5"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Product}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
