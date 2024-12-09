"""TestKnownGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.known_glyph import KnownGlyph
from src.glyphs.simple_text_glyph import SimpleTextGlyph
from src.glyphs.text_glyph import TextGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestKnownGlyph(TestGlyph):
    """Test suite for the KnownGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for KnownGlyph.

        Initializes the style, coordinates, and number for the KnownGlyph.
        """
        super().setUp()
        self.glyph = KnownGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self):
        """Get the target SVG markup for the KnownGlyph.

        Returns:
            str: The expected target SVG markup for the KnownGlyph.
        """
        return (
            '<g>'
            '<text class="StyleBackground" transform="translate(150.0, 150.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
            '<text class="StyleForeground" transform="translate(150.0, 150.0) ">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the KnownGlyph instance.

        Returns:
            str: The string representation of the KnownGlyph.
        """
        return "KnownGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that KnownGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, KnownGlyph, SimpleTextGlyph, TextGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
