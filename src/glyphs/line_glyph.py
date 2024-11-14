from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Line

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LineGlyph(Glyph):
    """Straight line between two points
    """

    def __init__(self, class_name: str, start: Coord, end: Coord):
        super().__init__(class_name)
        self.start = start
        self.end = end

    def draw(self) -> Optional[BaseElement]:
        return Line(start=self.start.point.coordinates, end=self.end.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.start!s}, {self.end!s})"
