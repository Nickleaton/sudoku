from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class ArrowGlyph(Glyph):
    arrow = "\u2191"  # ↑

    def __init__(self, class_name: str, angle: float, position: Coord):
        super().__init__(class_name)
        self.angle = Angle(float(angle))
        self.position = position

    def draw(self) -> Optional[BaseElement]:
        text = Text("",
                    transform=self.position.transform + " " + self.angle.transform,
                    class_=self.class_name)
        span = TSpan(ArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle!r}, {self.position!r})"
