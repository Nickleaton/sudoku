import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.first_n import FirstN
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestFirstN(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FirstN(self.board, Side.TOP, 1)

    @property
    def clazz(self):
        return FirstN

    @property
    def representation(self) -> str:
        return "FirstN(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 1)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, FirstN, Region}

    @property
    def config(self) -> str:
        return "FirstN: T1"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
