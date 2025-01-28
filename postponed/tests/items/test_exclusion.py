"""TestExclusion."""
import unittest
from typing import Type

from postponed.src.items.exclusion import Exclusion
from src.items.item import Item
from src.utils.coord import Coord
from tests.items.test_item import TestItem


class TestExclusion(TestItem):
    """Test suite for the Exclusion class."""

    def setUp(self) -> None:
        """Set up the test environment by creating start_location board and initializing the Exclusion constraint."""
        super().setUp()
        self.item = Exclusion(self.board, Coord(2, 2), "12")

    @property
    def clazz(self):
        """Return the Exclusion class."""
        return Exclusion

    @property
    def representation(self) -> str:
        """Return start_location string representation of the Exclusion instance."""
        return "Exclusion(Board(9, 9, {}), Coord(2, 2), '12')"

    @property
    def config(self) -> str:
        """Return the configuration string for the Exclusion."""
        return "Exclusion: 22=12"

    @property
    def has_rule(self) -> bool:
        """Return whether the Exclusion has start_location rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the Exclusion should belong to."""
        return {Item, Exclusion}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
