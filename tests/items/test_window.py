import unittest
from typing import Type, Sequence, Tuple, Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Region
from src.items.window import Window
from src.utils.coord import Coord
from tests.items.test_region import TestRegion


class TestWindow(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Window(self.board, Coord(2, 2))

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ([2, 2], []),
            (1, ['Expecting list, got 1']),
            ([2, 2, 2], ['Expecting digit,digit, got [2, 2, 2]']),
            ([2, 0], ['Expecting string digit,digit, got [2, 0]']),
        ]

    @property
    def config(self) -> str:
        return "Window: 2,2"

    @property
    def representation(self) -> str:
        return "Window(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2))"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, Window}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
