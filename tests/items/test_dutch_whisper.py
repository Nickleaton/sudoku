import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.variable_difference_pair import VariableDifferencePair
from src.items.dutch_whisper import DutchWhisper
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_greater_than_equal_difference_line import TestGreaterThanEqualDifferenceLine


class TestDutchWhispers(TestGreaterThanEqualDifferenceLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = DutchWhisper(self.board, cells)
        self.size = 5

    @property
    def clazz(self):
        return DutchWhisper

    @property
    def config(self) -> str:
        return "DutchWhisper: 11, 12, 13"

    @property
    def representation(self) -> str:
        return (
            "DutchWhisper"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, DifferenceLine, VariableDifferencePair, DutchWhisper, GreaterThanEqualDifferenceLine,
                GreaterThanEqualDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
