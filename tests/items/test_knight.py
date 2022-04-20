import unittest
from typing import Type, Sequence, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.knight import Knight
from tests.items.test_item import TestItem


class TestKnight(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Knight(self.board, [2, 4, 6, 8])

    @property
    def has_rule(self) -> bool:
        return True

    def test_offsets(self):
        self.assertEqual(8, len(self.item.offsets()))

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ([2, 4, 6, 8], []),
            (1, ['Expecting list, got 1']),
            ('xxx', ["Expecting list, got 'xxx'"]),
            ([0, 4, 6, 8], ['0 is not a valid digit']),
        ]

    @property
    def config(self) -> str:
        return "Knight: [2, 4, 6, 8]"

    @property
    def representation(self) -> str:
        return "Knight(Board(9, 9, 3, 3, None, None, None, None), [2, 4, 6, 8])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Knight, Cell}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
