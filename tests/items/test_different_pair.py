import unittest
from typing import Type, Sequence, Tuple, Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_pair import TestPair


class TestDifferentPair(TestPair):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = DifferentPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3), [1, 2])

    @property
    def representation(self) -> str:
        return (
            "DifferentPair"
            "("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3), "
            "[1, 2]"
            ")"
        )

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ({'Cells': [[1, 2], [1, 3]], 'Digits': [1, 2]}, []),
            ('xxx', ["Expecting dict, got 'xxx'"]),
            ({'Cells': [[1, 2], [1, 3]]}, ["Expecting two cells, plus digits got {'Cells': [[1, 2], [1, 3]]}"]),
            ({'Digits': [1, 2], 'xxx': 1}, ["Expecting Cells:, got {'Digits': [1, 2], 'xxx': 1}"]),
            ({'Cells': [[1, 2], [1, 3]], 'xxx': 1}, ["Expecting Digits:, got {'Cells': [[1, 2], [1, 3]], 'xxx': 1}"]),
            (
                {'Cells': [[1, 2]], 'Digits': [1, 2]},
                ["Expecting two Cells:, got {'Cells': [[1, 2]], 'Digits': [1, 2]}"]),
            ({'Cells': [[1, 2], [1, 3]], 'Digits': [2, 0]}, ['Invalid digit 0']),

        ]

    @property
    def config(self) -> str:
        return "Cells: [ [1, 2], [1, 3] ]\nDigits: 1,2"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Item, Pair, DifferentPair}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
