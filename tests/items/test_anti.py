import unittest
from typing import Type, List

from src.items.anti import Anti
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from tests.items.test_composed import TestComposed


class TestAnti(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = Anti(self.board, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.size = 0

    @property
    def clazz(self):
        return Anti

    def test_offsets(self):
        self.assertEqual(0, len(self.item.offsets()))

    @property
    def config(self) -> str:
        return "Anti: 1, 2, 3, 4, 5, 6, 7, 8, 9"

    @property
    def representation(self) -> str:
        return "Anti(Board(9, 9, 3, 3, None, None, None, None), [1, 2, 3, 4, 5, 6, 7, 8, 9])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, ComposedItem, Anti}

    @property
    def pair_output(self) -> List:
        return []

    def test_pairs(self):
        result = []
        for pair in self.item.pairs(Cell.make(self.board, 1, 1), self.item.digits):
            result.append([pair.cell_2.row, pair.cell_2.column])

        self.assertListEqual(sorted(self.pair_output), sorted(result))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
