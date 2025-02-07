"""TestSquareGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.glyphs.square_glyph import SquareGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestSquareGlyph(TestGlyph):
    """Test suite for the SquareGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for SquareGlyph.

        Initializes the style, coordinates, and size for the SquareGlyph.
        """
        super().setUp()
        self.glyph = SquareGlyph('SquareStyle', Coord(2, 3), 4)

    @property
    def target(self) -> str:
        """Expected SVG markup for the SquareGlyph.

        Returns:
            str: The expected SVG markup for the SquareGlyph, including a rectangle
            element with height, width, and transform attributes.
        """
        return (
            '<rect class="SquareStyle" height="400.0" '
            'transform="translate(300.0, 200.0)" width="400.0" '
            'x="0" y="0" />'
        )

    @property
    def representation(self) -> str:
        """Expected string representation of the SquareGlyph instance.

        Returns:
            str: The string representation of the SquareGlyph with style, coordinates, and size.
        """
        return "SquareGlyph('SquareStyle', Coord(2, 3), 4)"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Expected set of classes that SquareGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, RectGlyph, SquareGlyph}

    def test_svg_output(self) -> None:
        """Test that the SVG output matches the expected markup."""
        svg_element = self.glyph.draw()
        self.assertIsNotNone(svg_element, "The draw method should return an SVG element.")
        self.assertEqual(svg_element.tostring(), self.target)

    def test_representation(self) -> None:
        """Test the string representation of the SquareGlyph."""
        self.assertEqual(repr(self.glyph), self.representation)

    def test_inheritance(self) -> None:
        """Test that SquareGlyph inherits from the expected classes."""
        actual_classes = {cls for cls in self.glyph.__class__.__mro__ if issubclass(cls, Glyph)}
        self.assertEqual(actual_classes, self.expected_classes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
