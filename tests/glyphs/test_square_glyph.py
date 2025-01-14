"""TestSquareGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import SquareGlyph, RectGlyph
from src.utils.point import Point
from tests.glyphs.test_glyph import TestGlyph


class TestSquareGlyph(TestGlyph):
    """Test suite for the SquareGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for SquareGlyph.

        Initializes the style, position, and size for the SquareGlyph.
        """
        super().setUp()
        self.glyph = SquareGlyph('Style', position=Point(1000, 1000), size=5000)

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the SquareGlyph.

        Returns:
            str: The expected SVG markup for the square glyph as start rectangle element.
        """
        return '<rect class="Style" height="5000.0" transform="translate(1000.0, 1000.0)" width="5000.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the SquareGlyph instance.

        Returns:
            str: The string representation of the SquareGlyph with style, position, and size.
        """
        return "SquareGlyph('Style', Point(1000.0, 1000.0), 5000.0)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that SquareGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, RectGlyph, SquareGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
