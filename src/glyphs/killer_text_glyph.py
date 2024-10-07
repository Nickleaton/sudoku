from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class KillerTextGlyph(Glyph):

    def __init__(self, class_name: str, angle: float, position: Coord, text: str):
        super().__init__(class_name)
        self.angle = Angle(angle)
        self.position = position
        self.text = text

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        position = self.position.top_left + Coord(1, 1) * 0.05
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Background"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name + "Foreground"
                    )
        span = TSpan(self.text, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle}, {repr(self.position)}, '{self.text}')"
        )
