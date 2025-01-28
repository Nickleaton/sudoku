"""TestFrame."""
import unittest
from typing import Type

from postponed.src.items.first_n import FirstN
from postponed.src.items.frame import Frame
from postponed.tests.items.test_first_n import TestFirstN
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.utils.side import Side


class TestFrame(TestFirstN):
    """Test suite for the Frame class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the Frame constraint."""
        super().setUp()
        self.item = Frame(self.board, Side.top, 1, 20)
        self.size = 3

    @property
    def clazz(self):
        """Return the Frame class."""
        return Frame

    @property
    def representation(self) -> str:
        """Return start_location string representation of the Frame instance."""
        return "Frame(Board(9, 9, {}), Side.top, 20)"

    @property
    def config(self) -> str:
        """Return the configuration string for the Frame."""
        return "Frame: T1=20"

    @property
    def has_rule(self) -> bool:
        """Return True to indicate the rule is present for the Frame."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Frame should belong to."""
        return {Cell, ComposedItem, FirstN, Frame, Item, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
