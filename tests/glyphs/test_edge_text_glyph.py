"""TestEdgeTextGlyph."""
import unittest
from typing import Type

from src.glyphs.edge_text_glyph import EdgeTextGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.point import Point
from tests.glyphs.test_glyph import TestGlyph


class TestEdgeTextGlyph(TestGlyph):
    """Test suite for the EdgeTextGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for EdgeTextGlyph.

        Initializes an instance of EdgeTextGlyph with the given style, offset, and coordinates.
        """
        super().setUp()
        self.glyph = EdgeTextGlyph('Style', 0, Point(100.0, 100.0), Point(200.0, 100.0), 'X')

    @property
    def target(self) -> str:
        """Get the target SVG markup for EdgeTextGlyph.

        Returns:
            str: The SVG markup representing the EdgeTextGlyph, including both foreground and background text elements.
        """
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(150.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(150.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of EdgeTextGlyph.

        Returns:
            str: The string representation of the EdgeTextGlyph instance.
        """
        return "EdgeTextGlyph('Style', 0.0, Point(100.0, 100.0), Point(200.0, 100.0), 'X')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that EdgeTextGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {EdgeTextGlyph, Glyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
