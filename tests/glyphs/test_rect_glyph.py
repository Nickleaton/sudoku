"""TestRectGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestRectGlyph(TestGlyph):
    """Test suite for the RectGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for RectGlyph.

        Initializes the style and coordinates for the RectGlyph.
        """
        super().setUp()
        self.glyph = RectGlyph('Style', Coord(1, 1), Coord(2, 1))

    @property
    def target(self) -> str:
        """Expected SVG markup for the RectGlyph.

        Returns:
            str: The expected SVG markup for the RectGlyph, including rectangle
            element with height, width, and transform attributes.
        """
        return '<rect class="Style" height="200.0" transform="translate(100.0, 100.0)" width="100.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Expected string representation of the RectGlyph instance.

        Returns:
            str: The string representation of the RectGlyph with style, coordinates, and dimensions.
        """
        return "RectGlyph('Style', Coord(1, 1), Coord(2, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Expected set of classes that RectGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, RectGlyph}

    def test_svg_output(self) -> None:
        """Test that the SVG output matches the expected markup."""
        svg_element = self.glyph.draw()
        self.assertIsNotNone(svg_element, "The draw method should return an SVG element.")
        self.assertEqual(svg_element.tostring(), self.target)

    def test_representation(self) -> None:
        """Test the string representation of the RectGlyph."""
        self.assertEqual(repr(self.glyph), self.representation)

    def test_inheritance(self) -> None:
        """Test that RectGlyph inherits from the expected classes."""
        actual_classes = {cls for cls in self.glyph.__class__.__mro__ if issubclass(cls, Glyph)}
        self.assertEqual(actual_classes, self.expected_classes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
