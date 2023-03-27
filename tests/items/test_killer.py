import unittest
from typing import Type

from src.items.killer import Killer
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestKiller(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = Killer(self.board, 24, self.cells)
        self.size = 3

    @property
    def clazz(self):
        return Killer

    @property
    def representation(self) -> str:
        return "Killer(Board(9, 9, 3, 3, None, None, None, None), 24, " \
               "[Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), " \
               "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), " \
               "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, Item, Killer, Region}

    @property
    def config(self) -> str:
        return "Killer: 24=11,12,13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def inside(self) -> Cell:
        return Cell.make(self.board, 1, 2)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
