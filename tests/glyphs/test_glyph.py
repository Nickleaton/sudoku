import unittest
from typing import Type

from svgwrite import Drawing

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle

COLOURS = [
    "Red",
    "Orange",
    'Yellow',
    'Lime',
    'Green',
    'Cyan',
    'Blue',
    'Purple',
    'Magenta',
    'Grey'
]

a = Angle(0)  # Force imports for eval to work


class TestGlyph(unittest.TestCase):

    def setUp(self) -> None:
        self.canvas: Drawing = Drawing(filename="test.svg", size=("100%", "100%"))
        self.glyph: Glyph = Glyph('Style')
        self.maxDiff = None

    @property
    def representation(self) -> str:
        return "Glyph('Style')"

    @property
    def target(self) -> str:
        return ""  # pragma: no cover

    @property
    def start_marker(self) -> str:
        return ""

    @property
    def end_marker(self) -> str:
        return ""

    @property
    def symbol(self) -> str:
        return ""

    # pylint: disable=assignment-from-none
    def test_draw(self) -> None:
        if isinstance(self.glyph, Glyph):
            element = self.glyph.draw()
            if element is not None:
                self.assertEqual(self.target, element.tostring())

    def test_start_marker(self):
        marker = self.glyph.__class__.start_marker()
        if marker is None:
            self.assertEqual(self.start_marker, "", )
        else:
            self.assertEqual(self.start_marker, marker.tostring())

    def test_end_marker(self):
        marker = self.glyph.__class__.end_marker()
        if marker is None:
            self.assertEqual(self.end_marker, "")
        else:
            self.assertEqual(self.end_marker, marker.tostring())

    def test_symbol(self):
        symbol = self.glyph.__class__.symbol()
        if symbol is None:
            self.assertEqual(self.symbol, "")
        else:
            self.assertEqual(self.symbol, symbol.tostring())

    def test_priority(self):
        self.assertFalse(self.glyph < self.glyph)

    def test_repr(self):
        self.assertEqual(self.representation, str(self.glyph))

    # def test_eval_repr(self):
    #     # pylint: disable=eval-used
    #     self.assertEqual(self.representation, repr(eval(self.representation)))

    @property
    def expected_classes(self) -> set[Type[Glyph]]:
        return {Glyph}

    def test_used_classes(self) -> None:
        self.assertEqual(self.expected_classes, self.glyph.used_classes)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
