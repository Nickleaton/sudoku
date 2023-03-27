import unittest
from typing import Type

from src.items.cloned_region import ClonedRegion
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_item import TestItem
from tests.items.test_region import TestRegion


class TestClonedRegion(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.cells_1 = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.cells_2 = [Cell(self.board, 9, 9), Cell(self.board, 9, 8), Cell(self.board, 9, 7)]
        self.item = ClonedRegion(self.board, self.cells_1, self.cells_2)

    @property
    def clazz(self):
        return ClonedRegion

    @property
    def representation(self) -> str:
        return "ClonedRegion(Board(9, 9, 3, 3, None, None, None, None), " \
               "[Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), " \
               "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), " \
               "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)], " \
               "[Cell(Board(9, 9, 3, 3, None, None, None, None), 9, 9), " \
               "Cell(Board(9, 9, 3, 3, None, None, None, None), 9, 8), " \
               "Cell(Board(9, 9, 3, 3, None, None, None, None), 9, 7)]" \
                ")"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, ClonedRegion}

    @property
    def config(self) -> str:
        return "ClonedRegion: 11,12,13=99,98,97"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
