import unittest
from typing import Type

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.difference_line import DifferenceLine
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_line import TestLine


class TestDifferenceLine(TestLine):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = DifferenceLine(self.board, cells, 1)

    @property
    def representation(self) -> str:
        return (
            "DifferenceLine(Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, DifferenceLine, Item, Line, Region}

    @property
    def config(self) -> str:
        return f"{self.clazz.__name__}: [[1, 1], [1, 2], [1, 3]]"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.clazz.__name__, self.board, data[self.clazz.__name__])
        self.assertIsInstance(item, self.clazz)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
