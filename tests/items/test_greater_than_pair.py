import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.greater_than_pair import GreaterThanPair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_pair import TestPair


class TestGreaterThanPair(TestPair):
    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = GreaterThanPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))

    @property
    def clazz(self):
        return GreaterThanPair

    @property
    def config(self):
        return "GreaterThanPair: 12-13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def representation(self) -> str:
        return (
            "GreaterThanPair("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, GreaterThanPair, Item, Pair, ComposedItem, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
