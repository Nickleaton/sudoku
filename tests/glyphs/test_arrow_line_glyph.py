"""TestArrowLineGlyph."""
import unittest

from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_poly_line_glyph import TestPolyLineGlyph


class TestArrowLineGlyph(TestPolyLineGlyph):
    """Test suite for ArrowLineGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for ArrowLineGlyph.

        Initializes an instance of ArrowLineGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = ArrowLineGlyph('Style', [Coord(1, 1), Coord(2, 1), Coord(2, 2)])

    @property
    def start_marker(self) -> str:
        """Get the SVG marker for the start_location of the arrow.

        Returns:
            str: The SVG markup for the start_location marker.
        """
        return (
            '<marker class="Arrow ArrowStart" '
            'id="Arrow-start_location" '
            'markerHeight="35" '
            'markerWidth="35" '
            'refX="50" '
            'refY="50" '
            'viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="35" />'
            '</marker>'
        )

    @property
    def end_marker(self) -> str:
        """Get the SVG marker for the end_location of the arrow.

        Returns:
            str: The SVG markup for the end_location marker.
        """
        return (
            '<marker class="Arrow ArrowEnd" id="Arrow-end_location" markerHeight="20" markerWidth="20" orient="auto" '
            'refX="20" refY="20" viewBox="0 0 50 50"><polyline points="0,0 20,20 0,40" /></marker>'
        )

    @property
    def target(self):
        """Get the SVG markup for the polyline target.

        Returns:
            str: The SVG markup for the polyline target, including markers.
        """
        return (
            '<polyline class="Style" '
            'marker-end="url(#Style-end_location)" '
            'marker-start="url(#Style-start_location)" '
            'points="150.0,150.0 150.0,250.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of ArrowLineGlyph.

        Returns:
            str: The string representation of the ArrowLineGlyph instance.
        """
        return "ArrowLineGlyph('Style', [Coord(1, 1), Coord(2, 1), Coord(2, 2)])"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that ArrowLineGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {ArrowLineGlyph, Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
