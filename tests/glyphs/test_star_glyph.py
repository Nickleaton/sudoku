"""TestStarGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.glyphs.star_glyph import StarGlyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestStarGlyph(TestGlyph):
    """Test suite for the StarGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for StarGlyph.

        Initializes the style and position for the StarGlyph.
        """
        super().setUp()
        self.glyph = StarGlyph('Style', Coord(1, 1))

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the StarGlyph.

        Returns:
            str: The expected SVG markup for the star glyph as a group of text elements.
        """
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">✧</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(100, 100) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">✧</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the StarGlyph instance.

        Returns:
            str: The string representation of the StarGlyph with style and position.
        """
        return "StarGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that StarGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, SimpleTextGlyph, StarGlyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
