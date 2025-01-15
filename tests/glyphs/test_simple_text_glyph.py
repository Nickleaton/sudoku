"""TestSimpleTextGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestSimpleTextGlyph(TestGlyph):
    """Test suite for the SimpleTextGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for SimpleTextGlyph.

        Initializes the style, location, and text for the SimpleTextGlyph.
        """
        super().setUp()
        self.glyph = SimpleTextGlyph('Style', 0, Coord(1, 1), "X")

    @property
    def target(self) -> str:
        """Get the expected SVG markup for SimpleTextGlyph.

        Returns:
            str: The expected SVG markup for the SimpleTextGlyph, including background and foreground text elements.
        """
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100.0, 100.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">X</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the SimpleTextGlyph instance.

        Returns:
            str: The string representation of the SimpleTextGlyph with style, location, and text.
        """
        return "SimpleTextGlyph('Style', 0.0, Coord(1, 1), 'X')"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that SimpleTextGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, SimpleTextGlyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
