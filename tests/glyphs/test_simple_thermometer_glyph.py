"""TestSimpleThermometerGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.glyphs.simple_thermometer_glyph import SimpleThermometerGlyph
from src.glyphs.thermometer_glyph import ThermometerGlyph
from src.utils.coord import Coord
from tests.glyphs.test_thermometer_glyph import TestThermometerGlyph


class TestSimpleThermometerGlyph(TestThermometerGlyph):
    """Test suite for the SimpleThermometerGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for SimpleThermometerGlyph.

        Initializes the style and coordinates for the SimpleThermometerGlyph.
        """
        super().setUp()
        self.glyph = SimpleThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        """Get the expected marker for the start of the SimpleThermometerGlyph.

        Returns:
            str: The expected SVG markup for the start marker of the thermometer glyph.
        """
        return (
            '<marker class="SimpleThermometer SimpleThermometerStart" id="SimpleThermometer-start" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the SimpleThermometerGlyph.

        Returns:
            str: The expected SVG markup for the SimpleThermometerGlyph with start polyline and start marker.
        """
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the SimpleThermometerGlyph instance.

        Returns:
            str: The string representation of the SimpleThermometerGlyph with style and coordinates.
        """
        return "SimpleThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that SimpleThermometerGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, PolyLineGlyph, SimpleThermometerGlyph, ThermometerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
