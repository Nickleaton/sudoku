import unittest
from typing import Type, Sequence, Tuple, Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_pair import TestPair


class TestDifferencePair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DifferencePair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), 0)

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ({'Cells': [[1, 2], [1, 3]], 'Difference': 1}, []),
            ('xxx', ["Expecting dict, got 'xxx'"]),
            ({'Cells': [[1, 2], [1, 3]]}, ["Expecting two cells, plus difference {'Cells': [[1, 2], [1, 3]]}"]),
            ({'Difference': 1, 'xxx': 1}, ["Expecting Cells:, got {'Difference': 1, 'xxx': 1}"]),
            ({'Cells': [[1, 2], [1, 3]], 'xxx': 1},
             ["Expecting Difference:, got {'Cells': [[1, 2], [1, 3]], 'xxx': 1}"]),
            ({'Cells': [[1, 2]], 'Difference': 1}, ["Expecting two Cells:, got {'Cells': [[1, 2]], 'Difference': 1}"]),
            ({'Cells': [[1, 2], [1, 3]], 'Difference': 0}, ['Invalid digit 0']),

        ]

    @property
    def config(self) -> str:
        return "Cells: [[1, 2], [1, 3]]\nDifference: 1"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def difference(self) -> int:
        return 0

    @property
    def representation(self) -> str:
        return (
            "DifferencePair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "0"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, DifferencePair, Item, Pair}

    def test_difference(self):
        self.assertEqual(self.difference, self.item.difference)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
