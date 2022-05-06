import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.outside import Outside
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_first_n import TestFirstN


class TestOutside(TestFirstN):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Outside(self.board, Side.TOP, 1, [1, 2, 3])

    @property
    def clazz(self):
        return Outside

    @property
    def representation(self) -> str:
        return "Outside(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1, [1, 2, 3])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, FirstN, Item, Outside, Region}

    @property
    def config(self) -> str:
        return "Outside: T1=123"

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
