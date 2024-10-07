from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class LittleKillerGlyph(Glyph):
    arrow = "\uA71B"  # ꜛ

    def __init__(self, class_name: str, position: Coord, angle: Angle, value: int):
        super().__init__(class_name)
        self.position = position
        self.angle = angle
        self.value = value

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        position = (self.position + Coord(0.28, 0.28)).center
        text = Text("",
                    transform=position.transform,
                    class_=self.class_name
                    )
        span = TSpan(str(self.value), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        text = Text("",
                    transform=position.transform + " " + self.angle.transform,
                    class_=self.class_name
                    )
        span = TSpan(LittleKillerGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{repr(self.position)}, "
            f"{repr(self.angle)}, "
            f"{repr(self.value)}"
            f")"
        )
