import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.mountain import Mountain
from tests.items.test_line import TestLine


class TestMountain(TestLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell.make(self.board, 2, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 2, 3)]
        self.item = self.clazz(self.board, cells)

    @property
    def clazz(self):
        return Mountain

    @property
    def config(self) -> str:
        return "Mountain: 21, 12, 23"

    @property
    def representation(self) -> str:
        return (
            f"{self.clazz.__name__}(Board(9, 9, 3, 3, None, None, None, None), "
            f"["
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 2, 1), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 2, 3)"
            f"]"
            f")"
        )

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region, Mountain}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
