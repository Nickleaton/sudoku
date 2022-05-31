import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestDiagonal(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = Diagonal(self.board)
        self.size = 0

    @property
    def clazz(self):
        return Diagonal

    @property
    def representation(self) -> str:
        return "Diagonal(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Region, Diagonal}

    @property
    def config(self) -> str:
        return "Diagonal: "

    @property
    def has_rule(self) -> bool:
        return False

    def test_in(self):
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
