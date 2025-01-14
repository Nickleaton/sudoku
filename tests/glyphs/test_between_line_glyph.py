"""TestBetweenLineGlyph."""
import unittest
from typing import Type

from src.glyphs.between_line_glyph import BetweenLineGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.point import Point
from tests.glyphs.test_poly_line_glyph import TestPolyLineGlyph


class TestBetweenLineGlyph(TestPolyLineGlyph):
    """Test suite for BetweenLineGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for BetweenLineGlyph.

        Initializes an instance of BetweenLineGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = BetweenLineGlyph('Style', [Point(150, 150), Point(250, 150), Point(250, 250)])

    @property
    def start_marker(self) -> str:
        """Get the start marker SVG markup for BetweenLineGlyph.

        Returns:
            str: The SVG markup for the start marker of the BetweenLineGlyph.
        """
        return (
            '<marker class="Between BetweenStart" id="Between-start" markerHeight="35" markerWidth="35" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35" /></marker>'
        )

    @property
    def end_marker(self) -> str:
        """Get the end marker SVG markup for BetweenLineGlyph.

        Returns:
            str: The SVG markup for the end marker of the BetweenLineGlyph.
        """
        return (
            '<marker class="Between BetweenEnd" id="Between-end" markerHeight="35" markerWidth="35" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35" /></marker>'
        )

    @property
    def target(self) -> str:
        """Get the target SVG markup for BetweenLineGlyph.

        Returns:
            str: The SVG markup for the polyline representing the BetweenLineGlyph.
        """
        return (
            '<polyline class="Style" '
            'marker-end="url(#Style-end)" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of BetweenLineGlyph.

        Returns:
            str: The string representation of the BetweenLineGlyph instance.
        """
        return "BetweenLineGlyph('Style', [Point(150.0, 150.0), Point(250.0, 150.0), Point(250.0, 250.0)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that BetweenLineGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {BetweenLineGlyph, Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
