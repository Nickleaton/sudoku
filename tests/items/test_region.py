import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Region, StandardRegion
from tests.items.test_item import TestItem


class TestRegion(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = Region(self.board)
        self.item.add_items(cells)

    @property
    def config(self) -> str:
        return "Region:"

    @property
    def representation(self) -> str:
        return "Region(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region}


class TestStandardRegion(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = StandardRegion(self.board, 1)

    @property
    def config(self) -> str:
        return "StandardRegion: 1"

    @property
    def representation(self) -> str:
        return "StandardRegion(Board(9, 9, 3, 3, None, None, None, None), 1, [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Region, StandardRegion}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
