"""TestPolyLineGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestPolyLineGlyph(TestGlyph):
    """Test suite for the PolyLineGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for PolyLineGlyph.

        Initializes the style, coordinates, and polyline properties for the PolyLineGlyph.
        """
        super().setUp()
        self.glyph = PolyLineGlyph(
            "Style",
            [Coord(0, 0), Coord(2, 1), Coord(3, 2)],
            False,
            False
        )

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the PolyLineGlyph.

        Returns:
            str: The expected polyline SVG markup.
        """
        return '<polyline class="Style" points="50.0,50.0 150.0,250.0 250.0,350.0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the PolyLineGlyph instance.

        Returns:
            str: The string representation of the PolyLineGlyph.
        """
        return "PolyLineGlyph('Style', [Coord(0, 0), Coord(2, 1), Coord(3, 2)], False, False)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that PolyLineGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, PolyLineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
