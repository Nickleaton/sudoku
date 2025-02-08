"""TestArrowGlyph."""
import unittest

from src.glyphs.arrow_glyph import ArrowGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestArrowGlyph(TestGlyph):
    """Test suite for the ArrowGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for ArrowGlyph.

        Initialize the ArrowGlyph instance with specific parameters.
        """
        super().setUp()
        self.glyph = ArrowGlyph('Style', 90.0, Coord(0, 0))

    @property
    def start_marker(self) -> str:
        """Return the expected start_marker SVG markup for ArrowGlyph.

        Returns:
            str: The expected start_marker SVG markup.
        """
        return ''

    @property
    def end_marker(self) -> str:
        """Return the expected end_marker SVG markup for ArrowGlyph.

        Returns:
            str: The expected end_marker SVG markup.
        """
        return ''

    @property
    def symbol(self) -> str:
        """Return the expected symbol SVG markup for ArrowGlyph.

        Returns:
            str: The expected symbol SVG markup.
        """
        return ''

    @property
    def target(self):
        """Return the expected target SVG markup for ArrowGlyph.

        Returns:
            str: The expected target SVG markup.
        """
        return (
            '<text class="Style" transform="translate(0.0, 0.0) rotate(90.0)">'
            '<tspan alignment-baseline="central" text-anchor="middle">↑</tspan></text>'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of ArrowGlyph.

        Returns:
            str: The string representation of ArrowGlyph.
        """
        return 'ArrowGlyph(\'Style\', 90.0, Coord(0, 0))'

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Return the expected set of classes ArrowGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {ArrowGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
