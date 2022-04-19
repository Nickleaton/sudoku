import unittest
from typing import Type, Sequence, Any, Tuple

from src.items.board import Board
from src.items.frame import Frame
from src.items.item import Item
from src.utils.side import Side
from tests.items.test_item import TestItem


class TestFrame(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = Frame(self.board, Side.TOP, 1, 20)
        self.size = 9

    @property
    def representation(self) -> str:
        return "Frame(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, 20)"

    @property
    def valid_test_cases(self) -> Sequence[Tuple[Any, Sequence[str]]]:
        return [
            ("T1=20", []),
            ([], ['Expected str, got []']),
            ("T1", ["Expected side|index|total, got 'T1'"]),
            ("X1=20", ['Side not valid X']),
            ("T0=20", ['Index outside range 0']),
            ("TX=20", ['Index not valid X']),
            ("T1=xx", ['Invalid total xx'])
        ]

    @property
    def config(self) -> str:
        return "Frame: T1=20"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Frame, Item}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
