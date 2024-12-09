"""TestSimpleThermometer module."""

import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.simple_thermometer_line import SimpleThermometerLine
from src.items.thermometer_line import ThermometerLine
from tests.items.test_thermometer import TestThermometerLine


class TestSimpleThermometer(TestThermometerLine):
    """Test suite for the SimpleThermometerLine class."""

    @property
    def clazz(self):
        """Return the SimpleThermometerLine class."""
        return SimpleThermometerLine

    @property
    def config(self) -> str:
        """Return the configuration string for the SimpleThermometerLine."""
        return "SimpleThermometerLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        """Return whether the SimpleThermometerLine has start rule."""
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        """Return the expected set of classes for the SimpleThermometerLine."""
        return {Cell, ComposedItem, Item, Line, Region, SimpleThermometerLine, ThermometerLine}


if __name__ == '__main__':
    unittest.main()
