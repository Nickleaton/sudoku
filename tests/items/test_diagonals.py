import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.diagonals import TLBR, BLTR, Diagonal
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestDiagonal(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = Diagonal(self.board)

    @property
    def representation(self) -> str:
        return "Diagonal(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Region, Diagonal}

    @property
    def config(self) -> str:
        return "Diagonal: 1"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)

    @property
    def has_rule(self) -> bool:
        return True


class TestTLBR(TestDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = TLBR(self.board)

    @property
    def representation(self) -> str:
        return "TLBR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, Diagonal, TLBR}

    @property
    def config(self) -> str:
        return "TLBR:"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)


class TestBLTR(TestDiagonal):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3)
        self.item = BLTR(self.board)

    @property
    def representation(self) -> str:
        return "BLTR(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Cell, Region, Diagonal, BLTR}

    @property
    def config(self) -> str:
        return "BLTR:"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
