import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Region
from src.items.disjoint_group import DisjointGroup
from src.items.box import Box
from src.items.row import Row
from src.items.column import Column
from src.items.standard_region import StandardRegion
from src.items.region_sets import RegionSet, StandardRegionSet, Rows, DisjointGroups, Boxes, Columns
from tests.items.test_item import TestItem


class TestRegionSet(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = RegionSet(self.board, [])

    @property
    def config(self) -> str:
        return "RegionSet:"

    @property
    def representation(self) -> str:
        return "RegionSet(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed,  RegionSet}

    @property
    def has_rule(self) -> bool:
        return False


class TestStandardRegionSet(TestRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = StandardRegionSet(self.board, [])

    @property
    def config(self) -> str:
        return "StandardRegionSet:"

    @property
    def representation(self) -> str:
        return "StandardRegionSet(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return False


class TestColumns(TestStandardRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Columns(self.board)

    @property
    def config(self) -> str:
        return "Columns:"

    @property
    def representation(self) -> str:
        return "Columns(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, StandardRegion, Region, Column, Columns, StandardRegion, RegionSet,
                StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return True


class TestRows(TestStandardRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Rows(self.board)

    @property
    def config(self) -> str:
        return "Rows:"

    @property
    def representation(self) -> str:
        return "Rows(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, StandardRegion, Region, Row, Rows, StandardRegion, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return True


class TestBoxes(TestStandardRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Boxes(self.board)

    @property
    def config(self) -> str:
        return "Boxes:"

    @property
    def representation(self) -> str:
        return "Boxes(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, StandardRegion, Region, Box, Boxes, StandardRegion, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return True


class TestDisjointGroups(TestStandardRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DisjointGroups(self.board)

    @property
    def config(self) -> str:
        return "DisjointGroups:"

    @property
    def representation(self) -> str:
        return "DisjointGroups(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, StandardRegion, Region, DisjointGroup, DisjointGroups, RegionSet, StandardRegion,
                StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
