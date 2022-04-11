import unittest
from typing import Type

from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.items.line import Line
from src.items.region import Region
from src.items.thermometer import Thermometer, SimpleThermometer, FrozenThermometer
from tests.items.test_line import TestLine


class TestThermometer(TestLine):

    @property
    def clazz(self):
        return Thermometer

    @property
    def has_rule(self) -> bool:
        return False

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region, Thermometer}


class TestSimpleThermometer(TestThermometer):

    @property
    def clazz(self):
        return SimpleThermometer

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, Item, Line, Region, SimpleThermometer, Thermometer}


class TestFrozenThermometer(TestThermometer):

    @property
    def clazz(self):
        return FrozenThermometer

    @property
    def has_rule(self) -> bool:
        return True

    @property
    def expected_classes(self) -> set[Type[Item]]:
        return {Cell, Composed, FrozenThermometer, Item, Line, Region, Thermometer}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
