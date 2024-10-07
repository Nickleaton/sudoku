from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord
from src.utils.direction import Direction


class LittleArrowGlyph(Glyph):
    arrow = "\u25B2"  # ▲

    def __init__(self, class_name: str, position: Coord, location: int):
        super().__init__(class_name)
        self.position = position
        self.location = location

    def draw(self) -> Optional[BaseElement]:
        direction = Direction.direction(self.location)
        size = Coord(0.4, 0.4)
        position = self.position + size
        text = Text("",
                    transform=position.transform + " " + direction.angle.transform,
                    class_=self.class_name
                    )
        span = TSpan(LittleArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.position)}, {repr(self.location)})"
