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

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FixedProductPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), 1)
        self.size = 2

    @property
    def clazz(self):
        from src.items.fixed_product_pair import FixedProductPair
        return FixedProductPair

    @property
    def representation(self) -> str:
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
        return "FixedProductPair: 12-13=1"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair, FixedPair, FixedProductPair, ComposedItem, Region}

    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
