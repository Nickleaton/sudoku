import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Column, Region, StandardRegion
from tests.items.test_region import TestStandardRegion


class TestColumn(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Column(self.board, 1)

    @property
    def config(self) -> str:
        return "Column: 1"

    @property
    def representation(self) -> str:
        return "Column(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, StandardRegion, Column}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
