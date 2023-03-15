import unittest
from typing import Type

from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_different_pair import TestDifferencePair


class TestGreaterThanEqualDifferencePair(TestDifferencePair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = GreaterThanEqualDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            1
        )
        self.size = 2

    @property
    def clazz(self):
        return GreaterThanEqualDifferencePair

    @property
    def config(self) -> str:
        return "GreaterThanEqualDifferencePair: 12-13=1"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def difference(self) -> int:
        return 1

    @property
    def representation(self) -> str:
        return (
            "GreaterThanEqualDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "1"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, FixedDifferencePair, FixedPair, Item, Pair, GreaterThanEqualDifferencePair, ComposedItem, Region}

    def test_difference(self):
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
