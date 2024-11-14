from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.shapes import Circle
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class QuadrupleGlyph(Glyph):

    def __init__(self, class_name: str, position: Coord, numbers: str):
        super().__init__(class_name)
        self.position = position
        self.numbers = numbers

    def draw(self) -> Optional[BaseElement]:
        group = Group()
        circle = Circle(class_=self.class_name + "Circle", center=self.position.bottom_right.point.coordinates, r=35)
        group.add(circle)
        text = Text(class_=self.class_name + "Text", text="", transform=self.position.bottom_right.transform)
        span = TSpan(self.numbers, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)
        return group

    @property
    def priority(self) -> int:
        return 20

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {self.position!r}, '{self.numbers}')"
