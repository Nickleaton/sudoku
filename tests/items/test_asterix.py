import unittest
from typing import Type, Sequence, Tuple, Any

from src.items.asterix import Asterix
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.region import Region
from tests.items.test_region import TestRegion


class TestAsterix(TestRegion):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Asterix(self.board)

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ({}, []),
            (1, ['Expecting dict, got 1']),
        ]

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
        return {Item, Composed, Cell, Region, Asterix}

    def test_in(self):
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
