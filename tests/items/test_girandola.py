import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.girandola import Girandola
from src.items.item import Item
from src.items.region import Region
from src.items.special_region import SpecialRegion
from tests.items.test_special_region import TestSpecialRegion


class TestGirandola(TestSpecialRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Girandola(self.board)

    @property
    def clazz(self):
        return Girandola

    @property
    def config(self) -> str:
        return "Girandola:"

    @property
    def representation(self) -> str:
        return "Girandola(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Cell, Region, Girandola, SpecialRegion}

    def test_in(self):
        self.assertIn(Cell.make(self.board, 1, 1), self.item)
        self.assertNotIn(Cell.make(self.board, 8, 8), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
