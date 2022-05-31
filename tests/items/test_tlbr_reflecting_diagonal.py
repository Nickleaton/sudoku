import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.tlbr_refecting_diagonal import TLBRReflecting
from tests.items.test_diagonal import TestDiagonal


class TestTLBRReflecting(TestDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = TLBRReflecting(self.board)
        self.size = 9

    @property
    def clazz(self):
        return TLBRReflecting

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def representation(self) -> str:
        return "TLBRReflecting(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Cell, ComposedItem, Region, Diagonal, TLBRReflecting}

    @property
    def config(self) -> str:
        return "TLBRReflecting:"

    def test_in(self):
        self.assertIn(Cell.make(self.board, 1, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
