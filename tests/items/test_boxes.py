import unittest
from typing import Type

from src.items.board import Board
from src.items.box import Box
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Region
from src.items.region_sets import RegionSet, StandardRegionSet
from src.items.boxes import Boxes
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region_sets import TestStandardRegionSet


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


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
