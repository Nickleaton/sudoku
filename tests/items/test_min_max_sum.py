import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.min_max_sum import MinMaxSum
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_first_n import TestFirstN


class TestMinMaxSum(TestFirstN):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = MinMaxSum(self.board, Side.TOP, 1, 20)
        self.size = 3

    @property
    def clazz(self):
        return MinMaxSum

    @property
    def representation(self) -> str:
        return "MinMaxSum(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 20)"

    @property
    def config(self) -> str:
        return "MinMaxSum: T1=20"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, FirstN, MinMaxSum, Item, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
