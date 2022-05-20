import unittest
from typing import Type

from src.items.board import Board
from src.items.box import Box
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestBox(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Box(self.board, 1)

    @property
    def clazz(self):
        return Box

    @property
    def config(self) -> str:
        return "Box: 1"

    @property
    def representation(self) -> str:
        return "Box(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region, StandardRegion, Box}

    def test_in(self):
        self.assertIn(Cell.make(self.board, 2, 2), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
