import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.items.sum_pair import SumPair
from tests.items.test_pair import TestPair


class TestSumPair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = SumPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def total(self) -> int:
        return 0

    @property
    def representation(self) -> str:
        return (
            "SumPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, SumPair, Item, Pair}

    def test_total(self):
        self.assertEqual(self.total, self.item.total)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()