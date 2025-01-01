"""TestOrthogonallyAdjacent."""
import unittest
from typing import Type

from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.orthogonally_adjacent import OrthogonallyAdjacent
from tests.items.test_composed import TestComposed


class TestOrthogonallyAdjacent(TestComposed):
    """Test suite for the OrthogonallyAdjacent class."""

    def setUp(self) -> None:
        """Set up the test environment for OrthogonallyAdjacent."""
        super().setUp()
        self.item = OrthogonallyAdjacent(self.board)
        self.size = 0

    @property
    def clazz(self):
        """Return the OrthogonallyAdjacent class."""
        return OrthogonallyAdjacent

    @property
    def representation(self) -> str:
        """Return the string representation of the OrthogonallyAdjacent instance."""
        return "OrthogonallyAdjacent(Board(9, 9, 3, 3, None))"

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected classes that the OrthogonallyAdjacent instance should belong to."""
        return {OrthogonallyAdjacent, ComposedItem, Item}

    @property
    def config(self) -> str:
        """Return the configuration string for OrthogonallyAdjacent."""
        return "OrthogonallyAdjacent:"

    @property
    def has_rule(self) -> bool:
        """Return whether the OrthogonallyAdjacent instance has start rule."""
        return True


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
