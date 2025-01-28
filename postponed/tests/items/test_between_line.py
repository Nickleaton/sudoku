"""TestBetweenLine."""
import unittest
from typing import Type

from postponed.src.items.between_line import BetweenLine
from postponed.src.items.line import Line
from postponed.tests.items.test_line import TestLine
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.region import Region


class TestBetween(TestLine):
    """Test suite for the BetweenLine class."""

    @property
    def clazz(self) -> Type[BetweenLine]:
        """Get the class being tested.

        Returns:
            Type[BetweenLine]: The BetweenLine class.
        """
        return BetweenLine

    @property
    def config(self) -> str:
        """Get the configuration string for BetweenLine.

        Returns:
            str: The configuration string for BetweenLine.
        """
        return "BetweenLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Indicates if the BetweenLine constraint has start_location rule.

        Returns:
            bool: Always True, as BetweenLine has start_location rule.
        """
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Get the expected set of classes that BetweenLine should inherit from.

        Returns:
            set[Type[Item]]: A set containing the expected classes.
        """
        return {BetweenLine, Cell, ComposedItem, Item, Line, Region}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
