import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_pair import TestPair


class TestDifferencePair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DifferencePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def difference(self) -> int:
        return 0

    @property
    def representation(self) -> str:
        return (
            f"DifferencePair"
            f"("
            f"Board(9, 9, 3, 3, None, None, None, None), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            f")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, DifferencePair, Item, Pair}

    def test_difference(self):
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
