import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.disjoint_group import DisjointGroup
from src.items.item import Item
from src.items.region import Region
from src.items.standard_region import StandardRegion
from tests.items.test_standard_region import TestStandardRegion


class TestDisjointGroup(TestStandardRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DisjointGroup(self.board, 1)

    @property
    def config(self) -> str:
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


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
