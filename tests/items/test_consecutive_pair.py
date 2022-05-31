import unittest
from typing import Optional, Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.consecutive_pair import ConsecutivePair
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_difference_pair import TestDifferencePair


class TestConsecutivePair(TestDifferencePair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = ConsecutivePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        return ConsecutivePair

    @property
    def config(self) -> str:
        return "ConsecutivePair: 12-13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def representation(self) -> str:
        return (
            "ConsecutivePair("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def difference(self) -> Optional[int]:
        return 1

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ConsecutivePair, DifferencePair, Item, Pair, LessThanEqualDifferencePair, ComposedItem, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
