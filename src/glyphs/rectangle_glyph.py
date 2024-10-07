from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord
from src.utils.point import Point


class RectangleGlyph(Glyph):

    # pylint: disable=too-many-arguments
    def __init__(self,
                 class_name: str,
                 first: Coord,
                 second: Coord,
                 percentage: float,
                 ratio: float,
                 vertical: bool
                 ):
        super().__init__(class_name)
        self.first = first
        self.second = second
        self.percentage = percentage
        self.ratio = ratio
        self.vertical = vertical

    def draw(self) -> Optional[BaseElement]:
        if self.vertical:
            size = Point(config.drawing.cell_size * self.percentage * self.ratio,
                         config.drawing.cell_size * self.percentage)
        else:
            size = Point(config.drawing.cell_size * self.percentage,
                         config.drawing.cell_size * self.percentage * self.ratio)
        position = Coord.middle(self.first, self.second)
        return Rect(transform=position.transform, size=size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"{repr(self.first)}, "
            f"{repr(self.second)}, "
            f"{repr(self.percentage)}, "
            f"{repr(self.ratio)}, "
            f"{repr(self.vertical)}"
            f")"
        )
