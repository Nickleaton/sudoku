import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.sum_pair import SumPair
from src.items.xi_pair import XIPair
from tests.items.test_sum_pair import TestSumPair


class TestXIPair(TestSumPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = XIPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))

    @property
    def clazz(self):
        return XIPair

    @property
    def config(self):
        return "XIPair: 12-13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def total(self) -> int:
        return 11

    @property
    def representation(self) -> str:
        return (
            "XIPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, SumPair, Item, Pair, XIPair, ComposedItem, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
