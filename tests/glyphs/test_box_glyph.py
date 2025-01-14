"""TestBoxGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import BoxGlyph, RectGlyph
from src.utils.point import Point
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestBoxGlyph(TestSquareGlyph):
    """Test suite for BoxGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for BoxGlyph.

        Initializes an instance of BoxGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = BoxGlyph('Style', Point(100, 100), Point(300, 300))

    @property
    def target(self):
        """Get the SVG markup for BoxGlyph target.

        Returns:
            str: The SVG markup for the BoxGlyph target element.
        """
        return '<rect class="Style" height="300.0" transform="translate(100.0, 100.0)" width="300.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Return the string representation of BoxGlyph.

        Returns:
            str: The string representation of the BoxGlyph instance.
        """
        return "BoxGlyph('Style', Point(100.0, 100.0), Point(300.0, 300.0))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that BoxGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {BoxGlyph, Glyph, RectGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
