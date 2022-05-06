import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.entropic import Entropic
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestEntropic(TestLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [
            Cell.make(self.board, 1, 1),
            Cell.make(self.board, 1, 2),
            Cell.make(self.board, 1, 3),
            Cell.make(self.board, 1, 4),
            Cell.make(self.board, 1, 5),
            Cell.make(self.board, 1, 6)
        ]
        self.item = Entropic(self.board, cells)

    @property
    def config(self) -> str:
        return f"Entropic: 11, 12, 13, 14, 15, 16"

    @property
    def clazz(self):
        return Entropic

    @property
    def representation(self) -> str:
        return (
            "Entropic"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 4), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 5), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 6)"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Entropic, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
