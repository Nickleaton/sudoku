"""TestLittleKillerGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.little_killer_glyph import LittleKillerGlyph
from src.utils.coord import Coord
from src.utils.moves import Moves
from tests.glyphs.test_glyph import TestGlyph


class TestLittleKillerGlyph(TestGlyph):
    """Test suite for the LittleKillerGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for LittleKillerGlyph.

        Initializes the style, position, angle, and number for the LittleKillerGlyph.
        """
        super().setUp()
        self.glyph = LittleKillerGlyph('Style', Coord(0, 0), Moves.DOWN_RIGHT.angle, 20)

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the LittleKillerGlyph.

        Returns:
            str: The expected target SVG markup for the LittleKillerGlyph.
        """
        return (
            '<g>'
            '    <text class="Style" transform="translate(50.0, 50.0)">'
            '        <tspan alignment-baseline="central" text-anchor="middle">20</tspan>'
            '    </text>'
            '    <text class="Style" transform="translate(50.0, 50.0) rotate(315.0)">'
            '        <tspan alignment-baseline="central" text-anchor="middle">ꜛ</tspan>'
            '    </text>'
            '</g>'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the LittleKillerGlyph instance.

        Returns:
            str: The string representation of the LittleKillerGlyph.
        """
        return "LittleKillerGlyph('Style', Coord(0, 0), Angle(315.0), 20)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that LittleKillerGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, LittleKillerGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
