import unittest
from typing import Type

from src.items.asterix import Asterix
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.special_region import SpecialRegion
from tests.items.test_special_region import TestSpecialRegion


class TestAsterix(TestSpecialRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Asterix(self.board)
        self.size = 9

    @property
    def clazz(self):
        return Asterix

    @property
    def config(self) -> str:
        return "Asterix:"

    @property
    def representation(self) -> str:
        return "Asterix(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region, Asterix, SpecialRegion}

    def test_in(self):
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
