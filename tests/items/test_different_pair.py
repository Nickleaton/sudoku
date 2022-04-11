import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_pair import TestPair


class TestDifferentPair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DifferentPair(self.board, Cell(None, 1, 2), Cell(None, 1, 3), '12')

    @property
    def representation(self) -> str:
        return f"DifferentPair(Board(9, 9, 3, 3, None, None, None, None), Cell(None, 1, 2), Cell(None, 1, 3))"

    @property
    def config(self):
        return f"Cells: [ [1, 2], [1, 3] ]\nDigits: 1,2"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair, DifferentPair}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
