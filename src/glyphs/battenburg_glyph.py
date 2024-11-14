from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Marker, Symbol, Use
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.direction import Direction


class BattenburgGlyph(Glyph):
    """Battenburg

    CSS classes are BattenburgGlyphPink and BattenburgGlyphYellow
    """

    def __init__(self, class_name: str, coord: Coord):
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Marker]:
        result = Symbol(
            viewBox="0 0 100 100",
            id_="Battenberg-symbol",
            class_="Battenberg"
        )
        percentage = 0.3
        for i, position in enumerate([(d * percentage).point for d in Direction.orthogonals()]):
            result.add(
                Rect(
                    transform=position.transform,
                    size=Coord(percentage, percentage).point.coordinates,
                    class_="Battenberg" + ("Pink" if i % 2 == 0 else "Yellow")
                )
            )
        return result

    def draw(self) -> Optional[BaseElement]:
        return Use(
            href="#Battenberg-symbol",
            insert=self.coord.point.coordinates,
            class_="Battenberg",
            height=100,
            width=100
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.coord!r})"
