import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.simple_thermometer import SimpleThermometer
from src.items.thermometer import Thermometer
from tests.items.test_thermometer import TestThermometer


class TestSimpleThermometer(TestThermometer):

    @property
    def clazz(self):
        return SimpleThermometer

    @property
    def config(self) -> str:
        return f"SimpleThermometer: 11, 12, 13"

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region, SimpleThermometer, Thermometer}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
