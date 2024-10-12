import unittest
from typing import Type

from src.glyphs.composed_glyph import ComposedGlyph
from src.glyphs.glyph import Glyph
from tests.glyphs.test_glyph import TestGlyph


class TestComposedGlyph(TestGlyph):

    def setUp(self) -> None:
        super().setUp()
        self.glyph = ComposedGlyph('Style')

    @property
    def target(self):
        return '<g />'

    @property
    def representation(self) -> str:
        return (
            "ComposedGlyph("
            "'Style', "
            "["
            "]"
            ")"
        )

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {ComposedGlyph, Glyph}


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
