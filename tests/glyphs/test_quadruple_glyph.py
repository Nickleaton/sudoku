"""TestQuadrupleGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestQuadrupleGlyph(TestGlyph):
    """Test suite for the QuadrupleGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for QuadrupleGlyph.

        Initializes the style, coordinates, and number ('1234') for the QuadrupleGlyph.
        """
        super().setUp()
        self.glyph = QuadrupleGlyph("Style", Coord(2, 2), "1234")

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the QuadrupleGlyph.

        Returns:
            str: The expected SVG markup for the QuadrupleGlyph, including start circle and text elements.
        """
        return (
            '<g>'
            '<circle class="StyleCircle" cx="300" cy="300" r="35" />'
            '<text class="StyleText" transform="translate(300, 300)">'
            '<tspan alignment-baseline="central" text-anchor="middle">1234</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the QuadrupleGlyph instance.

        Returns:
            str: The string representation of the QuadrupleGlyph with style, coordinates, and number.
        """
        return "QuadrupleGlyph('Style', Coord(2, 2), '1234')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that QuadrupleGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, QuadrupleGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
