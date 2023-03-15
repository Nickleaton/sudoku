import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.anti_queen import AntiQueen
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_anti import TestAnti


class TestAntiQueen(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiQueen(self.board, [8, 9])
        self.size = 816

    @property
    def clazz(self):
        return AntiQueen

    def test_offsets(self):
        self.assertEqual(36, len(self.item.offsets()))

    @property
    def config(self) -> str:
        return "AntiQueen: 8, 9"

    @property
    def representation(self) -> str:
        return "AntiQueen(Board(9, 9, 3, 3, None, None, None, None), [8, 9])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiQueen, Cell, ComposedItem, DifferencePair, Item, Pair, Region}

    @property
    def pair_output(self) -> List:
        return [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
