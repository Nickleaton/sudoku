"""TestThermometer module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.thermometer_line import ThermometerLine
from tests.items.test_line import TestLine


class TestThermometerLine(TestLine):
    """Test case for ThermometerLine class."""

    @property
    def clazz(self):
        """Return the ThermometerLine class."""
        return ThermometerLine

    @property
    def config(self) -> str:
        """Return the configuration string for ThermometerLine."""
        return "ThermometerLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether ThermometerLine has a rule."""
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for ThermometerLine."""
        return {Cell, ComposedItem, Item, Line, Region, ThermometerLine}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
