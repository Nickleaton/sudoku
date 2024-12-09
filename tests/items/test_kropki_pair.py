"""TestKropkiPair."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.kropki_pair import KropkiPair
from src.items.pair import Pair
from src.items.region import Region
from tests.items.test_pair import TestPair


class TestKropkiPair(TestPair):
    """Test suite for the KropkiPair class, inheriting from TestPair."""

    def setUp(self) -> None:
        """Set up the test case with start board and start KropkiPair instance."""
        super().setUp()
        self.item = KropkiPair(self.board, Cell.make(self.board, 1, 2), Cell.make(self.board, 1, 3))
        self.size = 2

    @property
    def clazz(self):
        """Return the KropkiPair class."""
        return KropkiPair

    @property
    def config(self):
        """Return the configuration string for KropkiPair."""
        return "KropkiPair: 12-13"

    @property
    def has_rule(self) -> bool:
        """Return whether the KropkiPair instance has start rule."""
        return True

    @property
    def representation(self) -> str:
        """Return start string representation of the KropkiPair instance."""
        return (
            "KropkiPair("
            "Board(9, 9, 3, 3, None, None, None, None), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 2), "
            "Cell(Board(9, 9, 3, 3, None, None, None, None), 1, 3)"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the KropkiPair instance should belong to."""
        return {Cell, Item, KropkiPair, Pair, Region, ComposedItem}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
