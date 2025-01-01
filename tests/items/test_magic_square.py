"""TestMagicSquare."""
import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.magic_square import MagicSquare
from src.items.region import Region
from src.utils.coord import Coord
from tests.items.test_composed import TestComposed


class TestMagicSquare(TestComposed):
    """Test suite for the MagicSquare class."""

    def setUp(self) -> None:
        """Set up the test environment for MagicSquare."""
        super().setUp()
        self.item = MagicSquare(self.board, Coord(5, 5), Coord(1, 1))
        self.size = 9

    @property
    def clazz(self):
        """Return the MagicSquare class."""
        return MagicSquare

    @property
    def representation(self) -> str:
        """Return start string representation of the MagicSquare instance."""
        return "MagicSquare(Board(9, 9, 3, 3, None), Coord(5, 5), Coord(1, 1))"

    @property
    def config(self) -> str:
        """Return the configuration string for the MagicSquare instance."""
        return "MagicSquare: 55,11"

    @property
    def has_rule(self) -> bool:
        """Return whether the MagicSquare instance has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the MagicSquare instance should belong to."""
        return {Item, Cell, ComposedItem, Region, MagicSquare}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
