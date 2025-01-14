"""TestConsecutiveCircle1Glyph."""
import unittest
from typing import Type

from src.glyphs.consecutive1_glyph import Consecutive1Glyph
from src.glyphs.glyph import Glyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.point import Point
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestConsecutiveCircle1Glyph(TestCircleGlyph):
    """Test suite for the Consecutive1Glyph class."""

    def setUp(self) -> None:
        """Set up the test environment for Consecutive1Glyph.

        Initializes an instance of Consecutive1Glyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = Consecutive1Glyph('Style', Point(100, 100), Point(200, 100))

    @property
    def target(self) -> str:
        """Get the target SVG markup for Consecutive1Glyph.

        Returns:
            str: The SVG markup representing the Consecutive1Glyph, which in this case is start rectangle.
        """
        return '<rect class="Style" height="50.0" transform="translate(150.0, 100.0)" width="25.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Return the string representation of Consecutive1Glyph.

        Returns:
            str: The string representation of the Consecutive1Glyph instance.
        """
        return "Consecutive1Glyph('Style', Point(100.0, 100.0), Point(200.0, 100.0))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that Consecutive1Glyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {RectangleGlyph, Consecutive1Glyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
