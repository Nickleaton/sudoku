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
            Cell(self.board, 1, 1),
            Cell(self.board, 1, 2),
            Cell(self.board, 1, 3),
            Cell(self.board, 1, 4),
            Cell(self.board, 1, 5),
            Cell(self.board, 1, 6)
        ]
        self.item = Entropic(self.board, cells)

    @property
    def representation(self) -> str:
        return (
            f"Entropic"
            f"("
            f"Board(9, 9, 3, 3, None, None, None, None), "
            f"["
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 4), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 5), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 6)"
            f"]"
            f")"
        )

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Entropic, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
