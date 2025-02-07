"""TestBoxGlyph."""
import unittest

from src.glyphs.box_glyph import BoxGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestBoxGlyph(TestGlyph):
    """Test suite for the BoxGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for BoxGlyph.

        Initializes the style, coordinates, and dimensions for the BoxGlyph.
        """
        super().setUp()
        self.glyph = BoxGlyph('BoxStyle', Coord(3, 4), Coord(5, 6))

    @property
    def target(self) -> str:
        """Expected SVG markup for the BoxGlyph.

        Returns:
            str: The expected SVG markup for the BoxGlyph, including a rectangle
            element with height, width, and transform attributes.
        """
        return '<rect class="BoxStyle" height="500.0" transform="translate(400.0, 300.0)" width="600.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Expected string representation of the BoxGlyph instance.

        Returns:
            str: The string representation of the BoxGlyph with style, coordinates, and dimensions.
        """
        return "BoxGlyph('BoxStyle', Coord(3, 4), Coord(5, 6))"

    @property
    def expected_classes(self) -> set[type[Glyph]]:
        """Expected set of classes that BoxGlyph should inherit from.

        Returns:
            set[type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, RectGlyph, BoxGlyph}

    def test_svg_output(self) -> None:
        """Test that the SVG output matches the expected markup."""
        svg_element = self.glyph.draw()
        self.assertIsNotNone(svg_element, "The draw method should return an SVG element.")
        self.assertEqual(svg_element.tostring(), self.target)

    def test_representation(self) -> None:
        """Test the string representation of the BoxGlyph."""
        self.assertEqual(repr(self.glyph), self.representation)

    def test_inheritance(self) -> None:
        """Test that BoxGlyph inherits from the expected classes."""
        actual_classes = {cls for cls in self.glyph.__class__.__mro__ if issubclass(cls, Glyph)}
        self.assertEqual(actual_classes, self.expected_classes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
