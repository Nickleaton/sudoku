from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class RectGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord, size: Coord):
        super().__init__(class_name)
        self.position = position
        self.size = size

    def draw(self) -> Optional[BaseElement]:
        return Rect(transform=self.position.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.size)})"


class SquareGlyph(RectGlyph):

    def __init__(self, class_name: str, position: Coord, size: int):
        super().__init__(class_name, position, Coord(size, size))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.size.row)})"


class BoxGlyph(RectGlyph):

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.size)})"
