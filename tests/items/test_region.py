import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Region, StandardRegion, Column, Row, Box, DisjointGroup, Window
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestRegion(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = Region(self.board)
        self.item.add_items(cells)

    @property
    def config(self):
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
    def config(self):
        return "StandardRegion: 1"

    @property
    def representation(self) -> str:
        return "StandardRegion(Board(9, 9, 3, 3, None, None, None, None), 1, [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Region, StandardRegion}


class TestColumn(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Column(self.board, 1)

    @property
    def config(self):
        return "Column: 1"

    @property
    def representation(self) -> str:
        return "Column(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, StandardRegion, Column}


class TestRow(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Row(self.board, 1)

    @property
    def config(self):
        return "Row: 1"

    @property
    def representation(self) -> str:
        return "Row(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, StandardRegion, Row}


class TestBox(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Box(self.board, 1)

    @property
    def config(self):
        return "Box: 1"

    @property
    def representation(self) -> str:
        return "Box(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, StandardRegion, Box}


class TestDisjointGroup(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DisjointGroup(self.board, 1)

    @property
    def config(self):
        return "DisjointGroup: 1"

    @property
    def representation(self) -> str:
        return "DisjointGroup(Board(9, 9, 3, 3, None, None, None, None), 1)"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, StandardRegion, DisjointGroup}


class TestWindow(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Window(self.board, Coord(2, 2))

    @property
    def config(self):
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
