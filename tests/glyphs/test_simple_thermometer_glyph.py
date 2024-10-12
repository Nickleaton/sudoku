import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.glyphs.simple_thermometer_glyph import SimpleThermometerGlyph
from src.glyphs.thermometer_glyph import ThermometerGlyph
from src.utils.coord import Coord
from tests.glyphs.test_thermometer_glyph import TestThermometerGlyph


class TestSimpleThermometerGlyph(TestThermometerGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = SimpleThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        return (
            '<marker class="SimpleThermometer SimpleThermometerStart" id="SimpleThermometer-start" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self):
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        return "SimpleThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph, PolyLineGlyph, SimpleThermometerGlyph, ThermometerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
