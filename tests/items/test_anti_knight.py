import unittest
from typing import Optional, Type, List

from src.items.anti import Anti
from src.items.anti_knight import AntiKnight
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_anti import TestAnti


class TestAntiKnight(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = AntiKnight(self.board)

    def offset_length(self) -> Optional[int]:
        return 8

    @property
    def representation(self) -> str:
        return "AntiKnight(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiKnight, Cell, Composed, DifferentPair, Item, Pair}

    @property
    def config(self) -> str:
        return "AntiKnight:"

    @property
    def pair_output(self) -> List:
        return [[2, 3], [3, 2]]

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
