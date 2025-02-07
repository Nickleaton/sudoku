"""TestLineGlyph."""
import unittest

from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLineGlyph(TestGlyph):
    """Test suite for the LineGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for LineGlyph.

        Initializes the style, start_location coordinate, and end_location coordinate for the LineGlyph.
        """
        super().setUp()
        self.glyph = LineGlyph("Style", Coord(0, 0), Coord(2, 1))

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the LineGlyph.

        Returns:
            str: The expected target SVG markup for the LineGlyph.
        """
        return '<line class="Style" x1="0.0" x2="100.0" y1="0.0" y2="200.0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the LineGlyph instance.

        Returns:
            str: The string representation of the LineGlyph.
        """
        return "LineGlyph('Style', Coord(0, 0), Coord(2, 1))"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Get the expected set of classes that LineGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, LineGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
