import unittest
from typing import Type

from src.glyphs.between_line_glyph import BetweenLineGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_poly_line_glyph import TestPolyLineGlyph


class TestBetweenLineGlyph(TestPolyLineGlyph):
    """Test suite for BetweenLineGlyph class, verifying SVG markers, polyline rendering, and class hierarchy."""

    def setUp(self) -> None:
        """Set up the test environment for BetweenLineGlyph.

        Initializes an instance of BetweenLineGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = BetweenLineGlyph('Style', [Coord(1, 1), Coord(2, 1), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        """Get the start_location marker SVG markup for BetweenLineGlyph.

        Returns:
            str: The SVG markup for the start_location marker of the BetweenLineGlyph.
        """
        return (
            '<marker class="Between BetweenStart" id="Between-start_location" markerHeight="35.0" markerWidth="35.0" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35.0" /></marker>'
        )

    @property
    def end_marker(self) -> str:
        """Get the end_location marker SVG markup for BetweenLineGlyph.

        Returns:
            str: The SVG markup for the end_location marker of the BetweenLineGlyph.
        """
        return (
            '<marker class="Between BetweenEnd" id="Between-end_location" markerHeight="35.0" markerWidth="35.0" '
            'refX="50" refY="50" viewBox="0 0 100 100"><circle cx="50" cy="50" r="35.0" /></marker>'
        )

    @property
    def target(self) -> str:
        """Get the target SVG markup for BetweenLineGlyph.

        Returns:
            str: The SVG markup for the polyline representing the BetweenLineGlyph.
        """
        return (
            '<polyline class="Style" '
            'marker-end="url(#Style-end_location)" '
            'marker-start="url(#Style-start_location)" '
            'points="150.0,150.0 150.0,250.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of BetweenLineGlyph.

        Returns:
            str: The string representation of the BetweenLineGlyph instance.
        """
        return "BetweenLineGlyph('Style', [Coord(1, 1), Coord(2, 1), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that BetweenLineGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {BetweenLineGlyph, Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
