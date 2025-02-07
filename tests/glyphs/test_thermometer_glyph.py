"""TestThermometerGlyph."""
import unittest

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.glyphs.thermometer_glyph import ThermometerGlyph
from src.utils.coord import Coord
from tests.glyphs.test_poly_line_glyph import TestPolyLineGlyph


class TestThermometerGlyph(TestPolyLineGlyph):
    """Test suite for the ThermometerGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for ThermometerGlyph.

        Initializes the style and coordinates for the ThermometerGlyph.
        """
        super().setUp()
        self.glyph = ThermometerGlyph('Style', [Coord(1, 1), Coord(2, 1), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        """Get the expected SVG marker for the start_location of the thermometer.

        Returns:
            str: The expected SVG marker element for the thermometer start_location.
        """
        return (
            '<marker class="Thermometer ThermometerStart" id="Thermometer-start_location" refX="50" refY="50" '
            'viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the ThermometerGlyph.

        Returns:
            str: The expected SVG markup for the thermometer polyline with the specified marker.
        """
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start_location)" '
            'points="150.0,150.0 150.0,250.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the ThermometerGlyph instance.

        Returns:
            str: The string representation of the ThermometerGlyph with style and coordinates.
        """
        return "ThermometerGlyph('Style', [Coord(1, 1), Coord(2, 1), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that ThermometerGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, PolyLineGlyph, ThermometerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
