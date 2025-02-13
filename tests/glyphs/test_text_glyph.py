"""TestTextGlyph."""
import unittest

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestTextGlyph(TestGlyph):
    """Test suite for the TextGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for TextGlyph.

        Initializes the style, rotation, location, and text content for the TextGlyph.
        """
        super().setUp()
        self.glyph = TextGlyph('Style', 90, Coord(10, 10), "abcd")

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the TextGlyph.

        Returns:
            str: The expected SVG markup for the text glyph, including background and foreground text elements.
        """
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(1000.0, 1000.0) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(1000.0, 1000.0) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">abcd</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the TextGlyph instance.

        Returns:
            str: The string representation of the TextGlyph with style, rotation, location, and content.
        """
        return "TextGlyph('Style', 90.0, Coord(10, 10), 'abcd')"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that TextGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
