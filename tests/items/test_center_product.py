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

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = CenterProduct(self.board, Coord(2, 2), 5)

    @property
    def clazz(self):
        return CenterProduct

    @property
    def representation(self) -> str:
        return "CenterProduct(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2), 5)"

    @property
    def config(self) -> str:
        return "CenterProduct: 22=5"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, CenterProduct, ComposedItem, Item, Product, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
