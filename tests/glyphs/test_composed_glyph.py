"""TestComposedGlyph."""
import unittest
from typing import Type

from src.glyphs.composed_glyph import ComposedGlyph
from src.glyphs.glyph import Glyph
from tests.glyphs.test_glyph import TestGlyph


class TestComposedGlyph(TestGlyph):
    """Test suite for the ComposedGlyph class."""

    def setUp(self) -> None:
        """Set up the test environment for ComposedGlyph.

        Initializes an instance of ComposedGlyph with the given style.
        """
        super().setUp()
        self.glyph = ComposedGlyph('Style')

    @property
    def target(self) -> str:
        """Get the target SVG markup for ComposedGlyph.

        Returns:
            str: The SVG markup representing the ComposedGlyph, which in this case is an empty <g> element.
        """
        return '<g />'

    @property
    def representation(self) -> str:
        """Return the string representation of ComposedGlyph.

        Returns:
            str: The string representation of the ComposedGlyph instance.
        """
        return (
            "ComposedGlyph("
            "'Style', "
            "["
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        """Get the expected set of classes that ComposedGlyph should inherit from.

        Returns:
            set[Type[Glyph]]: A set containing the expected classes.
        """
        return {ComposedGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
