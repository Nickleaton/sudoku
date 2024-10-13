import unittest
from typing import Type

from src.items.between import Between
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestBetween(TestLine):

    def setUp(self) -> None:
        super().setUp()
        self.board = Board(9, 9, 3, 3, None, None, None, None)

    @property
    def clazz(self):
        return Between

    @property
    def config(self) -> str:
        return "Between: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Between, Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
