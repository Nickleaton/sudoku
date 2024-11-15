"""TestCircleGlyph."""
import unittest
from typing import Type

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestCircleGlyph(TestGlyph):
    """Test suite for the CircleGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for CircleGlyph.

        Initializes an instance of CircleGlyph with the given style, coordinates, and radius.
        """
        super().setUp()
        self.glyph = CircleGlyph('Style', Coord(1, 1), 0.5)

    @property
    def target(self) -> str:
        """Get the target SVG markup for CircleGlyph.

        Returns:
            str: The SVG markup for the circle representing the CircleGlyph.
        """
        return '<circle class="Style" cx="0" cy="0" r="50.0" transform="translate(100, 100)" />'

    @property
    def representation(self) -> str:
        """Return the string representation of CircleGlyph.

        Returns:
            str: The string representation of the CircleGlyph instance.
        """
        return "CircleGlyph('Style', Coord(1, 1), 0.5)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that CircleGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {CircleGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
