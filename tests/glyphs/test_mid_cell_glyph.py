"""TestMidCellGlyph."""
import unittest
from typing import Type

from src.glyphs.glyph import Glyph
from src.glyphs.mid_cell_glyph import MidCellGlyph
from src.utils.coord import Coord
from tests.glyphs.test_glyph import TestGlyph


class TestMidCellGlyph(TestGlyph):
    """Test suite for the MidCellGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for MidCellGlyph.

        Initializes the class name, location, and configuration for MidCellGlyph.
        """
        super().setUp()
        self.glyph = MidCellGlyph('Style', Coord(2, 3))

    @property
    def target(self) -> str:
        """Get the expected SVG rectangle element for the MidCellGlyph.

        Returns:
            str: The expected SVG rectangle element.
        """
        return '<rect class="Style" height="70.0" transform="translate(300.0, 200.0)" width="70.0" x="0" y="0"/>'

    @property
    def representation(self) -> str:
        """Get the string representation of the MidCellGlyph instance.

        Returns:
            str: The string representation of the MidCellGlyph.
        """
        return "MidCellGlyph('Style', Coord(2, 3))"

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that MidCellGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {Glyph, MidCellGlyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
