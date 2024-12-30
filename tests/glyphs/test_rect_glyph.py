"""TestRectGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestRectGlyph(TestGlyph):
    """Test suite for the RectGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for RectGlyph.

        Initializes the style and coordinates for the RectGlyph.
        """
        super().setUp()
        self.glyph = RectGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the RectGlyph.

        Returns:
            str: The expected SVG markup for the RectGlyph, including start rectangle element
            with height, width, and transform attributes.
        """
        return '<rect class="Style" height="100" transform="translate(100, 100)" width="200" digit1="0" digit2="0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the RectGlyph instance.

        Returns:
            str: The string representation of the RectGlyph with style, coordinates, and dimensions.
        """
        return "RectGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that RectGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, RectGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
