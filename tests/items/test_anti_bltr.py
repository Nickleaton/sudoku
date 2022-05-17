import unittest
from typing import Type

from src.items.anti_bltr import AntiBLTR
from src.items.anti_diagonal import AntiDiagonal
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from tests.items.test_anti_diagonal import TestAntiDiagonal


class TestAntiBLTR(TestAntiDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = AntiBLTR(self.board)

    @property
    def clazz(self):
        return AntiBLTR

    @property
    def representation(self) -> str:
        return "AntiBLTR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, Diagonal, AntiBLTR, AntiDiagonal}

    @property
    def config(self) -> str:
        return "AntiBLTR:"

    def test_in(self):
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
