import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.anti_monkey import AntiMonkey
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_anti import TestAnti


class TestAntiMonkey(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiMonkey(self.board)
        self.size = 384

    @property
    def clazz(self):
        return AntiMonkey

    def test_offsets(self):
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def representation(self) -> str:
        return "AntiMonkey(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiMonkey, Cell, ComposedItem, DifferencePair, Item, Pair, Region}

    @property
    def config(self) -> str:
        return "AntiMonkey:"

    @property
    def pair_output(self) -> List:
        return [[2, 4], [4, 2]]

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
