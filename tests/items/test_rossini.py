import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.region import Region
from src.items.rossini import Rossini
from src.utils.order import Order
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestRossini(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Rossini(self.board, Side.TOP, 1, Order.INCREASING)

    @property
    def clazz(self):
        return Rossini

    @property
    def representation(self) -> str:
        return "Rossini(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, Order.INCREASING)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, FirstN, Item, Region, Rossini}

    @property
    def config(self) -> str:
        return "Rossini: T1=I"

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
