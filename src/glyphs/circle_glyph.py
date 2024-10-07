from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord


class CircleGlyph(Glyph):
    """
    Circle
    """

    def __init__(self, class_name: str, center: Coord, percentage: float):
        super().__init__(class_name)
        self.center = center
        self.percentage = percentage

    @property
    def priority(self) -> int:
        return 10

    def draw(self) -> Optional[BaseElement]:
        return Circle(transform=self.center.point.transform, r=self.percentage * config.drawing.cell_size,
                      class_=self.class_name)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.center)}, {repr(self.percentage)})"
