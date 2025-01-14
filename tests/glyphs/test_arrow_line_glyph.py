"""TestArrowLineGlyph."""
import unittest
from typing import Type

from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.point import Point
from tests.glyphs.test_poly_line_glyph import TestPolyLineGlyph


class TestArrowLineGlyph(TestPolyLineGlyph):
    """Test suite for ArrowLineGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for ArrowLineGlyph.

        Initializes an instance of ArrowLineGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = ArrowLineGlyph(
            'Style',
            [Point(150, 150), Point(250, 150), Point(250, 250)]
        )

    @property
    def start_marker(self) -> str:
        """Get the SVG marker for the start of the arrow.

        Returns:
            str: The SVG markup for the start marker.
        """
        return (
            '<marker class="Arrow ArrowStart" '
            'id="Arrow-start" '
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
        """Get the SVG marker for the end of the arrow.

        Returns:
            str: The SVG markup for the end marker.
        """
        return (
            '<marker class="Arrow ArrowEnd" id="Arrow-end" markerHeight="20" markerWidth="20" orient="auto" '
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
            'marker-end="url(#Style-end)" '
            'marker-start="url(#Style-start)" '
            'points="150.0,150.0 250.0,150.0 250.0,250.0" />'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of ArrowLineGlyph.

        Returns:
            str: The string representation of the ArrowLineGlyph instance.
        """
        return "ArrowLineGlyph('Style', [Point(150.0, 150.0), Point(250.0, 150.0), Point(250.0, 250.0)])"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that ArrowLineGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {ArrowLineGlyph, Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
