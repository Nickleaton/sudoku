import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.difference_line import DifferenceLine
from src.items.difference_pair import DifferencePair
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.item import Item
from src.items.line import Line
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_line import TestLine


class TestGreaterThanEqualDifferenceLine(TestLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = GreaterThanEqualDifferenceLine(self.board, cells, 9)

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def representation(self) -> str:
        return (
            "GreaterThanEqualDifferenceLine"
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
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, DifferenceLine, DifferencePair, GreaterThanEqualDifferenceLine,
                GreaterThanEqualDifferencePair, Item, Line, Pair, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
