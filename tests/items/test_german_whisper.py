import unittest
from typing import Type

from src.items.fixed_difference_pair import FixedDifferencePair
from src.items.fixed_pair import FixedPair
from src.items.variable_pair import VariablePair
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.difference_line import DifferenceLine
from src.items.variable_difference_pair import VariableDifferencePair
from src.items.german_whisper import GermanWhisper
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_greater_than_equal_difference_line import TestGreaterThanEqualDifferenceLine


class TestGermanWhisper(TestGreaterThanEqualDifferenceLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = GermanWhisper(self.board, cells)
        self.size = 5

    @property
    def clazz(self):
        return GermanWhisper

    @property
    def config(self) -> str:
        return "GermanWhisper: 11, 12, 13"

    @property
    def representation(self) -> str:
        return (
            "GermanWhisper"
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
        return {Cell, ComposedItem, DifferenceLine, FixedDifferencePair, FixedPair, GermanWhisper,
                GreaterThanEqualDifferenceLine, GreaterThanEqualDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
