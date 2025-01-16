"""TestLittleArrowGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.little_arrow_glyph import LittleArrowGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLittleArrowGlyph(TestGlyph):
    """Test suite for the LittleArrowGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for LittleArrowGlyph.

        Initializes the style, location, and size for the LittleArrowGlyph.
        """
        super().setUp()
        self.glyph = LittleArrowGlyph('Style', Coord(1, 1), 5)

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the LittleArrowGlyph.

        Returns:
            str: The expected target SVG markup for the LittleArrowGlyph.
        """
        return (
            '<text class="Style" transform="translate(140.0, 140.0) rotate(135.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">▲</tspan>'
            '</text>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the LittleArrowGlyph instance.

        Returns:
            str: The string representation of the LittleArrowGlyph.
        """
        return "LittleArrowGlyph('Style', Coord(1, 1), 5)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that LittleArrowGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, LittleArrowGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
