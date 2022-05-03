import unittest
from typing import Type

from src.items.board import Board
from src.items.composed import Composed
from src.items.item import Item
from src.items.region_sets import StandardRegionSet, RegionSet
from tests.items.test_region_sets import TestRegionSet


class TestStandardRegionSet(TestRegionSet):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = StandardRegionSet(self.board, [])

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
        return {Item, Composed, RegionSet, StandardRegionSet}

    @property
    def has_rule(self) -> bool:
        return False


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
