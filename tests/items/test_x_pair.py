import unittest
from typing import Optional, Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.x_pair import XPair
from tests.items.test_difference_pair import TestDifferencePair


class TestXPair(TestDifferencePair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = XPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def difference(self) -> Optional[int]:
        return 10

    @property
    def representation(self) -> str:
        return (
            f"XPair"
            f"("
            f"Board(9, 9, 3, 3, None, None, None, None), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            f")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, DifferencePair, Item, Pair, XPair}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
