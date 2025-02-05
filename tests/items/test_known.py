"""TestKnown."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.even_cell import EvenCell
from src.items.fortress_cell import FortressCell
from src.items.high_cell import HighCell
from src.items.item import Item
from src.items.known import Known
from src.items.known_cell import KnownCell
from src.items.low_cell import LowCell
from src.items.mid_cell import MidCell
from src.items.odd_cell import OddCell
from src.items.simple_cell_reference import SimpleCellReference
from tests.items.test_composed import TestComposed


class TestKnown(TestComposed):
    """Test suite for the Known class, inheriting from TestComposed."""

    def setUp(self) -> None:
        """Set up the test case with start board and start Known instance."""
        super().setUp()
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
        self.item = Known(self.board, lines)

    @property
    def clazz(self):
        """Return the Known class."""
        return Known

    @property
    def config(self) -> str:
        """Return the configuration string for Known."""
        return (
            "Known:\n"
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
        """Return start string representation of the Known instance."""
        return (
            "Known(Board(9, 9, 3, 3, None), "
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
        """Return whether the Known instance has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Known instance should belong to."""
        return {
            Cell,
            CellReference,
            SimpleCellReference,
            ComposedItem,
            EvenCell,
            FortressCell,
            Item,
            KnownCell,
            Known,
            OddCell,
            LowCell,
            MidCell,
            HighCell
        }

    def test_flatten(self) -> None:
        """Test the flatten method of the Known instance."""
        expected = [self.item]
        for component in self.item.components:
            if isinstance(component, CellReference):
                expected.append(component)
                expected.append(component.cell)
        self.assertListEqual(expected, self.item.flatten())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
