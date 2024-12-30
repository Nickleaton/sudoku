"""TestCellGlyph."""
import unittest
from typing import Type

from src.glyphs.cell_glyph import CellGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph, SquareGlyph
from src.utils.coord import Coord
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestCellGlyph(TestSquareGlyph):
    """Test suite for the CellGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for CellGlyph.

        Initializes an instance of CellGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = CellGlyph('Style', Coord(1, 1))

    @property
    def target(self) -> str:
        """Get the target SVG markup for CellGlyph.

        Returns:
            str: The SVG markup for the rectangle representing the CellGlyph.
        """
        return '<rect class="Style" height="100" transform="translate(100, 100)" width="100" digit1="0" digit2="0" />'

    @property
    def representation(self) -> str:
        """Return the string representation of CellGlyph.

        Returns:
            str: The string representation of the CellGlyph instance.
        """
        return "CellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that CellGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {CellGlyph, Glyph, RectGlyph, SquareGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
