"""TestEvenCellGlyph."""
import unittest
from typing import Type

from src.glyphs.even_cell_glyph import EvenCellGlyph
from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestEvenCellGlyph(TestSquareGlyph):
    """Test suite for the EvenCellGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for EvenCellGlyph.

        Initializes an instance of EvenCellGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = EvenCellGlyph('Style', Coord(1, 1))

    @property
    def target(self) -> str:
        """Get the target SVG markup for EvenCellGlyph.

        Returns:
            str: The SVG markup representing the EvenCellGlyph.
        """
        return '<rect class="Style" height="70.0" transform="translate(115.0, 115.0)" width="70.0" x="0" y="0" />'

    @property
    def representation(self) -> str:
        """Return the string representation of EvenCellGlyph.

        Returns:
            str: The string representation of the EvenCellGlyph instance.
        """
        return "EvenCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that EvenCellGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {EvenCellGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
