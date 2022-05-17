import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.diagonals import Diagonal
from src.items.item import Item
from src.items.region import Region
from src.items.standard_diagonal import StandardDiagonal
from tests.items.test_diagonal import TestDiagonal


class TestStandardDiagonal(TestDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = StandardDiagonal(self.board)

    @property
    def clazz(self):
        return StandardDiagonal

    @property
    def representation(self) -> str:
        return "StandardDiagonal(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Region, Diagonal, StandardDiagonal}

    @property
    def config(self) -> str:
        return "StandardDiagonal: "

    @property
    def has_rule(self) -> bool:
        return True

    def test_in(self):
        self.assertNotIn(Cell.make(self.board, 1, 2), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
