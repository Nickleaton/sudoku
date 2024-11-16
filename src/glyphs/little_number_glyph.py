from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LittleNumberGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord, number: int):
        super().__init__(class_name)
        self.position = position
        self.number = number

    def draw(self) -> Optional[BaseElement]:
        size = Coord(0.35, 0.35)
        position = self.position + size
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.number), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, {self.number!r})"
