import unittest
from typing import Type, Sequence, Tuple, Any

import oyaml as yaml

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from tests.items.test_item import TestItem


class TestLine(TestItem):

    @property
    def clazz(self):
        return Line

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        cells = [Cell(self.board, 1, 1), Cell(self.board, 1, 2), Cell(self.board, 1, 3)]
        self.item = self.clazz(self.board, cells)

    @property
    def representation(self) -> str:
        return (
            f"{self.clazz.__name__}(Board(9, 9, 3, 3, None, None, None, None), "
            f"["
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 1), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            f"Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            f"]"
            f")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region}

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ([[1, 1], [1, 2], [1, 3]], []),
            ('xxxx', ["Expecting list, got 'xxxx'"]),
            ([[1, 1, 3], [1, 2], [1, 3]], ['Expecting pair, got [1, 1, 3]']),
            ([1, [1, 2], [1, 3]], ['Expecting list pair, got 1']),
            ([[1, 'a'], [1, 2], [1, 3]], ["Expecting int, got 'a'"]),
            ([['a', 1], [1, 2], [1, 3]], ["Expecting int, got 'a'"]),
            ([[1, 0], [1, 2], [1, 3]], ['Invalid row, column got [1, 0]']),
        ]

    @property
    def config(self) -> str:
        return f"{self.clazz.__name__}: [[1, 1], [1, 2], [1, 3]]"

    def test_create(self):
        data = yaml.load(self.config, yaml.SafeLoader)
        item = Item.create(self.clazz.__name__, self.board, data[self.clazz.__name__])
        self.assertIsInstance(item, self.clazz)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
