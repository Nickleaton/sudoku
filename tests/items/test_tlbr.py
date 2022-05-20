import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.standard_diagonal import StandardDiagonal
from src.items.tlbr import TLBR
from tests.items.test_standard_diagonal import TestStandardDiagonal


class TestTLBR(TestStandardDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = TLBR(self.board)

    @property
    def clazz(self):
        return TLBR

    @property
    def representation(self) -> str:
        return "TLBR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region, Diagonal, StandardDiagonal, TLBR}

    @property
    def config(self) -> str:
        return "TLBR:"

    def test_in(self):
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
