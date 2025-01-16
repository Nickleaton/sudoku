"""TestLowCellGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.low_cell_glyph import LowCellGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestLowCellGlyph(TestGlyph):
    """Test suite for the LowCellGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for LowCellGlyph.

        Initializes the class name and location for LowCellGlyph.
        """
        super().setUp()
        self.glyph = LowCellGlyph('Style', Coord(4, 5))

    @property
    def symbol(self) -> str:
        """Get the expected symbol SVG markup for the LowCellGlyph.

        Returns:
            str: The expected symbol SVG markup.
        """
        return (
            '<symbol class="LowCell" id="LowCell-symbol" viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="35.0" />'
            '</symbol>'
        )

    @property
    def target(self) -> str:
        """Get the expected SVG use element for the LowCellGlyph.

        Returns:
            str: The expected SVG use element for the LowCellGlyph.
        """
        return '<use class="LowCell" height="100" width="100" x="500.0" xlink:href="#LowCell-symbol" y="400.0" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the LowCellGlyph instance.

        Returns:
            str: The string representation of the LowCellGlyph.
        """
        return "LowCellGlyph('Style', Coord(4, 5))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that LowCellGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, LowCellGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
