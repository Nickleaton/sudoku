import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.magic_square import MagicSquare
from src.utils.coord import Coord
from tests.items.test_composed import TestComposed


class TestMagicSquare(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = MagicSquare(self.board, Coord(5, 5), Coord(1, 1))
        self.size = 9

    @property
    def representation(self) -> str:
        return "MagicSquare(Board(9, 9, 3, 3, None, None, None, None), Coord(5, 5), Coord(1, 1))"

    @property
    def config(self) -> str:
        return "Center: [5, 5]\nCorner: [1, 1]"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.item.__class__.__name__, self.board, data)
        self.assertIsNotNone(item)
        self.assertEqual(self.item.__class__, item.__class__)

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Cell, Composed, MagicSquare}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
