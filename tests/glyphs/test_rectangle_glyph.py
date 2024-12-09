"""TestRectangleGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rectangle_glyph import RectangleGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestRectangleGlyph(TestGlyph):
    """Test suite for the RectangleGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for RectangleGlyph.

        Initializes the style, coordinates, and dimensions for the RectangleGlyph.
        """
        super().setUp()
        self.glyph = RectangleGlyph('Style', Coord(1, 1), Coord(1, 2), 0.25, 2, True)

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the RectangleGlyph.

        Returns:
            str: The expected SVG markup for the RectangleGlyph, including rectangle element
                 with height, width, and transform attributes.
        """
        return (
            '<rect class="Style" height="25.0" transform="translate(150.0, 100.0)" '
            'width="50.0" x_coord="0" y_coord="0" />'
        )

    @property
    def representation(self) -> str:
        """Get the string representation of the RectangleGlyph instance.

        Returns:
            str: The string representation of the RectangleGlyph with style, coordinates, and dimensions.
        """
        return "RectangleGlyph('Style', Coord(1, 1), Coord(1, 2), 0.25, 2, True)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that RectangleGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, RectangleGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
