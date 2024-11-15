"""TestVariableDifferencePair."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.pair import Pair
from src.items.region import Region
from src.items.variable_difference_pair import VariableDifferencePair
from src.items.variable_pair import VariablePair
from tests.items.test_variable_pair import TestVariablePair


class TestVariableDifferencePair(TestVariablePair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = VariableDifferencePair(
            self.board,
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            "variable"
        )
        self.size = 2

    @property
    def clazz(self):
        return VariableDifferencePair

    @property
    def representation(self) -> str:
        return (
            "VariableDifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "'variable'"
            ")"
        )

    @property
    def config(self) -> str:
        return "VariableDifferencePair: 12-13=variable"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair, VariablePair, VariableDifferencePair, ComposedItem, Region}

    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

