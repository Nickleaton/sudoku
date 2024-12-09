"""TestFortressCellGlyph."""
import unittest
from typing import Type

from src.glyphs.fortress_cell_glyph import FortressCellGlyph
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import RectGlyph, SquareGlyph
from src.utils.coord import Coord
from tests.glyphs.test_square_glyph import TestSquareGlyph


class TestFortressCellGlyph(TestSquareGlyph):
    """Test suite for the FortressCellGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for FortressCellGlyph.

        Initializes an instance of FortressCellGlyph with the given style and coordinates.
        """
        super().setUp()
        self.glyph = FortressCellGlyph('Style', Coord(1, 1))

    @property
    def target(self) -> str:
        """Get the target SVG markup for FortressCellGlyph.

        Returns:
            str: The SVG markup representing the FortressCellGlyph.
        """
        return (
            '<rect class="Style" height="100" '
            'transform="translate(100, 100)" width="100" x_coord="0" y_coord="0" />'
        )

    @property
    def representation(self) -> str:
        """Return the string representation of FortressCellGlyph.

        Returns:
            str: The string representation of the FortressCellGlyph instance.
        """
        return "FortressCellGlyph('Style', Coord(1, 1))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that FortressCellGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {FortressCellGlyph, Glyph, RectGlyph, SquareGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
