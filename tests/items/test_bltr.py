import unittest
from typing import Type

from src.items.bltr import BLTR
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.standard_diagonal import StandardDiagonal
from tests.items.test_standard_diagonal import TestStandardDiagonal


class TestBLTR(TestStandardDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = BLTR(self.board)
        self.size = 9

    @property
    def clazz(self):
        return BLTR

    @property
    def representation(self) -> str:
        return "BLTR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region, Diagonal, StandardDiagonal, BLTR}

    @property
    def config(self) -> str:
        return "BLTR:"

    def test_in(self):
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
