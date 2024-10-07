from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class EvenCellGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord):
        super().__init__(class_name)
        self.position = position
        self.percentage = 0.7
        self.size = Coord(1, 1) * self.percentage

    def draw(self) -> Optional[BaseElement]:
        top_left = self.position + Coord(1, 1) * (1.0 - self.percentage) / 2.0
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)})"
