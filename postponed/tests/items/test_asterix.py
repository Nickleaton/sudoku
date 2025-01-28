"""TestAsterix."""
import unittest
from typing import Type

from postponed.src.items.asterix import Asterix
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region
from src.items.special_region import SpecialRegion
from tests.items.test_special_region import TestSpecialRegion


class TestAsterix(TestSpecialRegion):
    """Test suite for the Asterix class."""

    def setUp(self) -> None:
        """Set up the test environment for Asterix.

        Initializes the board and Asterix constraint with the default configuration.
        """
        super().setUp()
        self.item = Asterix(self.board)
        self.size = 9

    @property
    def clazz(self) -> Type[Asterix]:
        """Get the class being tested.

        Returns:
            Type[Asterix]: The Asterix class.
        """
        return Asterix

    @property
    def config(self) -> str:
        """Get the configuration string for Asterix.

        Returns:
            str: The configuration string for Asterix.
        """
        return "Asterix:"

    @property
    def representation(self) -> str:
        """Get the string representation of the Asterix instance.

        Returns:
            str: The string representation of the Asterix object.
        """
        return "Asterix(Board(9, 9, {}))"

    @property
    def has_rule(self) -> bool:
        """Indicates if the Asterix constraint has start_location rule.

        Returns:
            bool: Always True, as Asterix has start_location rule.
        """
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that Asterix should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {Item, ComposedItem, Cell, Region, Asterix, SpecialRegion}

    def test_in(self):
        """Test the inclusion of cells in the Asterix constraint.

        Asserts that start_location specific cell is included and another is not.
        """
        self.assertIn(Cell.make(self.board, 5, 5), self.item)
        self.assertNotIn(Cell.make(self.board, 9, 9), self.item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
