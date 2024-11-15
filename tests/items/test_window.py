"""TestWindow."""
import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.window import Window
from src.utils.coord import Coord
from tests.items.test_region import TestRegion


class TestWindow(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Window(self.board, Coord(2, 2))
        self.size = 9

    @property
    def clazz(self):
        return Window

    @property
    def config(self) -> str:
        return "Window: 22"

    @property
    def representation(self) -> str:
        return "Window(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2))"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region, Window}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

