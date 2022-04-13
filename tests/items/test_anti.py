import unittest
from typing import Optional, Type, List

from src.items.anti import Anti, AntiKnight, AntiKing, AntiMonkey, AntiQueen
from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.items.pair import Pair
from tests.items.test_item import TestItem


class TestAnti(TestItem):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = Anti(self.board, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def offset_length(self) -> Optional[int]:
        return 0

    def test_offsets(self):
        self.assertEqual(self.offset_length(), len(self.item.offsets()))

    @property
    def config(self) -> str:
        return "Anti: [1, 2, 3, 4, 5, 6, 7, 8, 9]"

    @property
    def representation(self) -> str:
        return "Anti(Board(9, 9, 3, 3, None, None, None, None), [1, 2, 3, 4, 5, 6, 7, 8, 9])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Item, Composed, Anti}

    @property
    def pair_output(self) -> List:
        return []

    def test_pairs(self):
        result = []
        for pair in self.item.pairs(Cell(self.board, 1, 1), self.item.digits):
            result.append([pair.c2.row, pair.c2.column])
        self.assertListEqual(self.pair_output, result)


class TestAntiKnight(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.item = AntiKnight(self.board)

    def offset_length(self) -> Optional[int]:
        return 8

    @property
    def representation(self) -> str:
        return "AntiKnight(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiKnight, Cell, Composed, DifferentPair, Item, Pair}

    @property
    def config(self) -> str:
        return "AntiKnight:"

    @property
    def pair_output(self) -> List:
        return [[2, 3], [3, 2]]

    @property
    def has_rule(self) -> bool:
        return True


class TestAntiMonkey(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiMonkey(self.board)

    def offset_length(self) -> Optional[int]:
        return 8

    @property
    def representation(self) -> str:
        return "AntiMonkey(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiMonkey, Cell, Composed, DifferentPair, Item, Pair}

    @property
    def config(self) -> str:
        return "AntiMonkey:"

    @property
    def pair_output(self) -> List:
        return [[2, 4], [4, 2]]

    @property
    def has_rule(self) -> bool:
        return True


class TestAntiKing(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiKing(self.board)

    def offset_length(self) -> Optional[int]:
        return 8

    @property
    def representation(self) -> str:
        return "AntiKing(Board(9, 9, 3, 3, None, None, None, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiKing, Cell, Composed, DifferentPair, Item, Pair}

    @property
    def config(self) -> str:
        return "AntiKing:"

    @property
    def pair_output(self) -> List:
        return [[2, 2], [1, 2], [2, 1]]

    @property
    def has_rule(self) -> bool:
        return True


class TestAntiQueen(TestAnti):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        Cell.make_board(self.board)
        self.item = AntiQueen(self.board, [8, 9])

    def offset_length(self) -> Optional[int]:
        return 36

    @property
    def config(self) -> str:
        return "AntiQueen: [8, 9]"

    @property
    def representation(self) -> str:
        return "AntiQueen(Board(9, 9, 3, 3, None, None, None, None), [8, 9])"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Anti, AntiQueen, Cell, Composed, DifferentPair, Item, Pair}

    @property
    def pair_output(self) -> List:
        return [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]

    @property
    def has_rule(self) -> bool:
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
