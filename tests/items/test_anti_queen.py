import unittest
from typing import Optional, Type, List

from src.items.anti import Anti
from src.items.anti_queen import AntiQueen
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_anti import TestAnti


class TestAntiQueen(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiQueen(self.board, [8, 9])

    def offset_length(self) -> Optional[int]:
        return 36

    @property
    def config(self) -> str:
        return "AntiQueen: [8, 9]"

    @property
    def representation(self) -> str:
        return "AntiQueen(Board(9, 9, 3, 3, None, None, None, None), [8, 9])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiQueen, Cell, Composed, DifferentPair, Item, Pair}

    @property
    def pair_output(self) -> List:
        return [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()