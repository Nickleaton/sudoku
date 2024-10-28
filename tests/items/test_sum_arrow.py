import unittest
from typing import Type

from src.items.sum_arrow_line import SumArrowLine
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestSumArrowLine1(TestLine):

    @property
    def clazz(self):
        return SumArrowLine

    @property
    def config(self) -> str:
        return "SumArrowLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {SumArrowLine, Cell, ComposedItem, Item, Line, Region}


class TestSumArrowLine2(TestLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2)]
        self.item = self.clazz(self.board, cells)
        self.size = 2

    @property
    def clazz(self):
        return SumArrowLine

    @property
    def config(self) -> str:
        return "SumArrowLine: 11, 12"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {SumArrowLine, Cell, ComposedItem, Item, Line, Region}

    @property
    def representation(self) -> str:
        return (
            f"{self.clazz.__name__}(Board(9, 9, 3, 3, None, None, None, None), "
            f"["
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2)"
            f"]"
            f")"
        )


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
