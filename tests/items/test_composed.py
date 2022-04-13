import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed, Constraints
from src.items.indexing import ColumnIndexer, Indexer
from src.items.item import Item
from src.items.region import Column, Row, Box, StandardRegion, Region
from src.items.region_sets import Boxes, Columns, Rows, RegionSet, StandardRegionSet
from tests.items.test_item import TestItem


class TestComposed(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Composed(self.board, [])
        self.size = 0

    def test_construction(self):
        self.assertEqual(self.size, len(self.item.items))

    def test_iteration(self):
        count = 0
        for _ in self.item:
            count += 1
        self.assertEqual(self.size, count)

    @property
    def config(self) -> str:
        return "Composed:"

    @property
    def representation(self) -> str:
        return "Composed(Board(9, 9, 3, 3, None, None, None, None), [])"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed}


class TestConstraints(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Constraints(self.board)
        self.item.add(Columns(self.board))
        self.item.add(Rows(self.board))
        self.item.add(Boxes(self.board))
        self.item.add(ColumnIndexer(self.board, 1))
        self.size = 4

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

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data['Constraints'])
        self.assertIsNotNone(item)

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Box, Boxes, Cell, Column, ColumnIndexer, Columns, Composed, Constraints, Indexer, Item, Region,
                RegionSet, Row, Rows, StandardRegion, StandardRegionSet}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
