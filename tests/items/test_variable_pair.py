import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.variable_pair import VariablePair
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_pair import TestPair


class TestVariablePair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = VariablePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), "variable")
        self.size = 2

    @property
    def clazz(self):
        return VariablePair

    @property
    def representation(self) -> str:
        return (
            "VariablePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "'variable'"
            ")"
        )

    @property
    def config(self) -> str:
        return "VariablePair: 12-13=variable"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair, VariablePair, ComposedItem, Region}

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 1, 2)

    def test_variable(self):
        self.assertEqual("variable", self.item.var_name)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
