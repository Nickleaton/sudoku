import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.fixed_pair import FixedPair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_pair import TestPair


class TestFixedPair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = FixedPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), 1)
        self.size = 2

    @property
    def clazz(self):
        return FixedPair

    @property
    def representation(self) -> str:
        return (
            "FixedPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "1"
            ")"
        )

    @property
    def difference(self) -> int:
        return 1

    @property
    def config(self) -> str:
        return "FixedPair: 12-13=1"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair, FixedPair, ComposedItem, Region}

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 1, 2)

    def test_difference(self):
        self.assertEqual(self.difference, self.item.value)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
