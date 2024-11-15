"""TestFrozenThermometerGlyph."""
import unittest
from typing import Type

from src.glyphs.frozen_thermometer_glyph import FrozenThermometerGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.glyphs.thermometer_glyph import ThermometerGlyph
from src.utils.coord import Coord
from tests.glyphs.test_thermometer_glyph import TestThermometerGlyph


class TestFrozenThermometerGlyph(TestThermometerGlyph):
    """Test suite for the FrozenThermometerGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for FrozenThermometerGlyph.

        Initializes an instance of FrozenThermometerGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = FrozenThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        """Get the start marker SVG markup for FrozenThermometerGlyph.

        Returns:
            str: The SVG markup representing the start marker of the FrozenThermometerGlyph.
        """
        return (
            '<marker class="FrozenThermometer FrozenThermometerStart" id="FrozenThermometer-start" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="30" /></marker>'
        )

    @property
    def target(self) -> str:
        """Get the target polyline SVG markup for FrozenThermometerGlyph.

        Returns:
            str: The SVG markup representing the polyline of the FrozenThermometerGlyph.
        """
        return (
            '<polyline class="Style" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of FrozenThermometerGlyph.

        Returns:
            str: The string representation of the FrozenThermometerGlyph instance.
        """
        return "FrozenThermometerGlyph('Style', [Coord(1, 1), Coord(1, 2), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that FrozenThermometerGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {FrozenThermometerGlyph, Glyph, PolyLineGlyph, ThermometerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
