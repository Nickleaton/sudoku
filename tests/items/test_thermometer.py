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

    @property
    def clazz(self):
        return ThermometerLine

    @property
    def config(self) -> str:
        return "ThermometerLine: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, ComposedItem, Item, Line, Region, ThermometerLine}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
