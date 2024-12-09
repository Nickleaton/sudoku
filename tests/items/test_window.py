"""TestWindow."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.window import Window
from src.utils.coord import Coord
from tests.items.test_region import TestRegion


class TestWindow(TestRegion):
    """Test suite for the Window class."""

    def setUp(self) -> None:
        """Set up the board and Window constraint for testing."""
        super().setUp()
        self.item = Window(self.board, Coord(2, 2))
        self.size = 9

    @property
    def clazz(self):
        """Return the Window class."""
        return Window

    @property
    def config(self) -> str:
        """Return the configuration string for Window."""
        return "Window: 22"

    @property
    def representation(self) -> str:
        """Return the string representation of the Window."""
        return "Window(Board(9, 9, 3, 3, None, None, None, None), Coord(2, 2))"

    @property
    def has_rule(self) -> bool:
        """Return whether Window has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for Window."""
        return {Item, ComposedItem, Cell, Region, Window}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
