import unittest
from typing import Type

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.even_cell import EvenCell
from src.items.fortress_cell import FortressCell
from src.items.high_cell import HighCell
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.knowns import Knowns
from src.items.low_cell import LowCell
from src.items.mid_cell import MidCell
from src.items.odd_cell import OddCell
from tests.items.test_composed import TestComposed


class TestKnowns(TestComposed):

    def setUp(self) -> None:
        self.board = Board(9, 9, 3, 3, None, None, None, None)
        self.size = 26
        lines = [
            "8..4.6..3",
            "o.9....2.",
            "e.......1",
            "f..h..m..",
            ".6.....l.",
            "..3..2..9",
            "7.2.3....",
            ".4....5..",
            "5..7.9..8"
        ]

        self.item = Knowns(self.board, lines)

    @property
    def clazz(self):
        return Knowns

    @property
    def config(self) -> str:
        return (
            "Knowns:\n"
            "  - 8..4.6..3\n"
            "  - o.9....2.\n"
            "  - e.......1\n"
            "  - f..h..m..\n"
            "  - .6.....l.\n"
            "  - ..3..2..9\n"
            "  - 7.2.3....\n"
            "  - .4....5..\n"
            "  - 5..7.9..8\n"
        )

    @property
    def representation(self) -> str:
        return (
            "Knowns(Board(9, 9, 3, 3, None, None, None, None), "
            "["
            "'8..4.6..3', "
            "'o.9....2.', "
            "'e.......1', "
            "'f..h..m..', "
            "'.6.....l.', "
            "'..3..2..9', "
            "'7.2.3....', "
            "'.4....5..', "
            "'5..7.9..8'"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {
            Cell,
            CellReference,
            ComposedItem,
            EvenCell,
            FortressCell,
            Item,
            KnownCell,
            Knowns,
            OddCell,
            LowCell,
            MidCell,
            HighCell
        }

    def test_flatten(self) -> None:
        expected = [self.item]
        for item in self.item.items:
            if isinstance(item, CellReference):
                expected.append(item)
                expected.append(item.cell)
        self.assertListEqual(expected, self.item.flatten())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
