"""TestKnown."""
import unittest

from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.known import Known
from src.items.known_cell import KnownCell
from tests.items.test_composed import TestComposed


class TestKnown(TestComposed):
    """Test suite for the Known class, inheriting from TestComposed."""

    def setUp(self) -> None:
        """Set up the test case with start_location board and start_location Known instance."""
        super().setUp()
        self.size = 20
        lines = (
            "8..4.6..3",
            "..9....2.",
            "........1",
            ".........",
            ".6.......",
            "..3..2..9",
            "7.2.3....",
            ".4....5..",
            "5..7.9..8"
        )
        self.item = Known(self.board, list(lines))

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
            "  - ..9....2.\n"
            "  - ........1\n"
            "  - .........\n"
            "  - .6.......\n"
            "  - ..3..2..9\n"
            "  - 7.2.3....\n"
            "  - .4....5..\n"
            "  - 5..7.9..8\n"
        )

    @property
    def representation(self) -> str:
        """Return start_location string representation of the Known instance."""
        return (
            "Known(Board(Coord(9, 9), Digits(1, 9), Tags({})), "
            "["
            "'8..4.6..3', "
            "'..9....2.', "
            "'........1', "
            "'.........', "
            "'.6.......', "
            "'..3..2..9', "
            "'7.2.3....', "
            "'.4....5..', "
            "'5..7.9..8'"
            "]"
            ")"
        )

    @property
    def has_rule(self) -> bool:
        """Return whether the Known instance has start_location rule."""
        return False

    @property
    def expected_classes(self) -> set[type[Item]]:
        """Return the expected classes that the Known instance should belong to."""
        return {
            Cell,
            CellReference,
            ComposedItem,
            Item,
            KnownCell,
            Known,
        }

    def test_flatten(self) -> None:
        """Test the flatten method of the Known instance."""
        expected = [self.item]
        expected.extend(
            [
                item for component in self.item.components
                for item in (component, component.cell)
                if isinstance(component, CellReference)
            ]
        )
        self.assertListEqual(expected, self.item.flatten())


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
