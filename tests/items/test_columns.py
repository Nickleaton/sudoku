import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.column import Column
from src.items.columns import Columns
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.region_sets import RegionSet, StandardRegionSet
from src.items.standard_region import StandardRegion
from tests.items.test_rows import TestStandardRegionSet


class TestColumns(TestStandardRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Columns(self.board)
        self.size = 9

    @property
    def clazz(self):
        return Columns

    @property
    def config(self) -> str:
        return "Columns:"

    @property
    def representation(self) -> str:
        return "Columns(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, StandardRegion, Region, Column, Columns, StandardRegion, RegionSet,
                StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
