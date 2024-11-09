import unittest
from typing import Type

from src.items.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region_set import RegionSet
from src.items.standard_region_set import StandardRegionSet
from tests.items.test_region_sets import TestRegionSet


class TestStandardRegionSet(TestRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = StandardRegionSet(self.board, [])
        self.size = 0

    @property
    def clazz(self):
        return StandardRegionSet

    @property
    def config(self) -> str:
        return "StandardRegionSet:"

    @property
    def representation(self) -> str:
        return "StandardRegionSet(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return False


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
