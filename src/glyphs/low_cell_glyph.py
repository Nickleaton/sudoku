from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LowCellGlyph(Glyph):

    def __init__(self, class_name: str, coord: Coord):
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Symbol]:
        result = Symbol(
            viewBox="0 0 100 100",
            id_="LowCell-symbol",
            class_="LowCell"
        )
        result.add(Circle(center=(50, 50), r=35))
        return result

    def draw(self) -> Optional[BaseElement]:
        return Use(href="#LowCell-symbol", insert=self.coord.point.coordinates, class_="LOwCell", height=100, width=100)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.coord!r})"
