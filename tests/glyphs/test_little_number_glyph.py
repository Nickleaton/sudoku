"""TestLittleNumberGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.little_number_glyph import LittleNumberGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLittleNumberGlyph(TestGlyph):
    """Test suite for the LittleNumberGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for LittleNumberGlyph.

        Initializes the style, position, and number for the LittleNumberGlyph.
        """
        super().setUp()
        self.glyph = LittleNumberGlyph('Style', Coord(1, 1), 1)

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the LittleNumberGlyph.

        Returns:
            str: The expected target SVG markup for the LittleNumberGlyph.
        """
        return (
            '<text class="Style" transform="translate(135.0, 135.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">1</tspan>'
            '</text>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the LittleNumberGlyph instance.

        Returns:
            str: The string representation of the LittleNumberGlyph.
        """
        return "LittleNumberGlyph('Style', Coord(1, 1), 1)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that LittleNumberGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, LittleNumberGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
