import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_composed import TestComposed


class TestRegion(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.cells = [Cell.make(self.board, 1, 1), Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3)]
        self.item = Region(self.board)
        self.item.add_items(self.cells)
        self.size = 3

    @property
    def clazz(self):
        return Region

    @property
    def config(self) -> str:
        return "Region:"

    @property
    def representation(self) -> str:
        return "Region(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region}

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 1, 1)

    @property
    def outside(self) -> Cell:
        return Cell.make(self.board, 9, 9)

    def test_in(self):
        self.assertIn(self.inside, self.item)
        self.assertNotIn(self.outside, self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
