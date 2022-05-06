import unittest
from typing import Type

from src.items.board import Board
from src.items.box import Box
from src.items.boxes import Boxes
from src.items.cell import Cell
from src.items.column import Column
from src.items.column_indexer import ColumnIndexer
from src.items.columns import Columns
from src.items.composed import Composed
from src.items.constraints import Constraints
from src.items.indexing import Indexer
from src.items.item import Item
from src.items.region import Region
from src.items.region_sets import RegionSet, StandardRegionSet
from src.items.row import Row
from src.items.rows import Rows
from src.items.standard_region import StandardRegion
from tests.items.test_composed import TestComposed


class TestConstraints(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Constraints(self.board)
        self.item.add(Columns(self.board))
        self.item.add(Rows(self.board))
        self.item.add(Boxes(self.board))
        self.item.add(ColumnIndexer(self.board, 1))
        self.size = 4

    @property
    def clazz(self):
        return Constraints

    def test_construction(self):
        self.assertEqual(self.size, len(self.item.items))

    def test_iteration(self):
        count = 0
        for _ in self.item:
            count += 1
        self.assertEqual(self.size, count)

    @property
    def representation(self) -> str:
        return (
            "Constraints(Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Columns(Board(9, 9, 3, 3, None, None, None, None)), "
            "Rows(Board(9, 9, 3, 3, None, None, None, None)), "
            "Boxes(Board(9, 9, 3, 3, None, None, None, None)), "
            "ColumnIndexer(Board(9, 9, 3, 3, None, None, None, None), 1)"
            "]"
            ")"
        )

    @property
    def config(self) -> str:
        return (
            "Constraints:\n"
            "  - Columns:\n"
            "  - Rows:\n"
            "  - Boxes:\n"
            "  - ColumnIndexer: 1\n"
        )

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Box, Boxes, Cell, Column, ColumnIndexer, Columns, Composed, Constraints, Indexer, Item, Region,
                RegionSet, Row, Rows, StandardRegion, StandardRegionSet}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
