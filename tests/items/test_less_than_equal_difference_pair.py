import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.pair import Pair
from tests.items.test_difference_pair import TestDifferencePair


class TestLessThanEqualDifferencePair(TestDifferencePair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = LessThanEqualDifferencePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def difference(self) -> int:
        return 0

    @property
    def representation(self) -> str:
        return (
            "LessThanEqualDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, DifferencePair, Item, Pair, LessThanEqualDifferencePair}

    def test_difference(self):
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
