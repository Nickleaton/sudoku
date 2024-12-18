"""TestOddCellGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.odd_cell_glyph import OddCellGlyph
from src.utils.coord import Coord
from tests.glyphs.test_circle_glyph import TestCircleGlyph


class TestOddCellGlyph(TestCircleGlyph):
    """Test suite for the OddCellGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for OddCellGlyph.

        Initializes the style and position for the OddCellGlyph.
        """
        super().setUp()
        self.glyph = OddCellGlyph('Style', Coord(1, 1))

    @property
    def symbol(self) -> str:
        """Get the expected symbol SVG markup for the OddCellGlyph.

        Returns:
            str: The expected symbol SVG markup.
        """
        return (
            '<symbol class="OddCell" id="OddCell-symbol" viewBox="0 0 100 100">'
            '<circle cx="50" cy="50" r="35" /></symbol>'
        )

    @property
    def target(self) -> str:
        """Get the expected SVG markup for the OddCellGlyph.

        Returns:
            str: The expected target SVG markup for the OddCellGlyph.
        """
        return '<use class="OddCell" height="100" width="100" row="100" xlink:href="#OddCell-symbol" column="100" />'

    @property
    def representation(self) -> str:
        """Get the string representation of the OddCellGlyph instance.

        Returns:
            str: The string representation of the OddCellGlyph.
        """
        return "OddCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that OddCellGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, OddCellGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
