"""TestLittleKiller."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.little_killer import LittleKiller
from src.items.region import Region
from src.utils.cyclic import Cyclic
from src.utils.side import Side
from tests.items.test_region import TestRegion


class TestLittleKiller1(TestRegion):
    """Test suite for the LittleKiller class (Case 1)."""

    def setUp(self) -> None:
        """Set up the test case, initializing the constraint and board for the LittleKiller instance (Case 1)."""
        super().setUp()
        self.item = LittleKiller(self.board, Side.TOP, Cyclic.CLOCKWISE, 3, 20)
        self.size = 6

    @property
    def clazz(self):
        """Return the LittleKiller class."""
        return LittleKiller

    @property
    def representation(self) -> str:
        """Return the string representation of the LittleKiller instance (Case 1)."""
        return "LittleKiller(Board(9, 9, 3, 3, None, None, None, None), Side.TOP, Cyclic.CLOCKWISE, 3, 20)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the LittleKiller instance should belong to (Case 1)."""
        return {Cell, ComposedItem, Item, LittleKiller, Region}

    @property
    def config(self) -> str:
        """Return the configuration string for the LittleKiller instance (Case 1)."""
        return "LittleKiller: T3C=20"

    @property
    def has_rule(self) -> bool:
        """Return whether the LittleKiller instance has start rule (Case 1)."""
        return True

    @property
    def inside(self) -> Cell:
        """Return the inside cell for the LittleKiller instance (Case 1)."""
        return Cell.make(self.board, 1, 4)


class TestLittleKiller2(TestRegion):
    """Test suite for the LittleKiller class (Case 2)."""

    def setUp(self) -> None:
        """Set up the test case, initializing the constraint and board for the LittleKiller instance (Case 2)."""
        super().setUp()
        self.item = LittleKiller(self.board, Side.RIGHT, Cyclic.CLOCKWISE, 3, 20)
        self.size = 6

    @property
    def clazz(self):
        """Return the LittleKiller class."""
        return LittleKiller

    @property
    def representation(self) -> str:
        """Return the string representation of the LittleKiller instance (Case 2)."""
        return "LittleKiller(Board(9, 9, 3, 3, None, None, None, None), Side.RIGHT, Cyclic.CLOCKWISE, 3, 20)"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the LittleKiller instance should belong to (Case 2)."""
        return {Cell, ComposedItem, Item, LittleKiller, Region}

    @property
    def config(self) -> str:
        """Return the configuration string for the LittleKiller instance (Case 2)."""
        return "LittleKiller: R3C=20"

    @property
    def has_rule(self) -> bool:
        """Return whether the LittleKiller instance has start rule (Case 2)."""
        return True

    @property
    def inside(self) -> Cell:
        """Return the inside cell for the LittleKiller instance (Case 2)."""
        return Cell.make(self.board, 9, 4)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
