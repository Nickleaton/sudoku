"""TestConsecutiveGlyph."""
import unittest
from typing import Type

from src.glyphs.consecutive_glyph import ConsecutiveGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestConsecutiveGlyph(TestCircleGlyph):
    """Test suite for the ConsecutiveGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for ConsecutiveGlyph.

        Initializes an instance of ConsecutiveGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = ConsecutiveGlyph('Style', Coord(1, 1), Coord(1, 2))

    @property
    def target(self) -> str:
        """Get the target SVG markup for ConsecutiveGlyph.

        Returns:
            str: The SVG markup representing the ConsecutiveGlyph, which in this case is a rectangle.
        """
        return '<rect class="Style" height="50.0" transform="translate(150.0, 100.0)" width="25.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Return the string representation of ConsecutiveGlyph.

        Returns:
            str: The string representation of the ConsecutiveGlyph instance.
        """
        return "ConsecutiveGlyph('Style', Coord(1, 1), Coord(1, 2))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that ConsecutiveGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {RectangleGlyph, ConsecutiveGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
