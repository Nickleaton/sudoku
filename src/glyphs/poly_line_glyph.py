from typing import List, Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Polyline

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class PolyLineGlyph(Glyph):
    """Polyline is a line through a list of coordinates
    """

    def __init__(self, class_name: str, coords: List[Coord], start: bool, end: bool):
        super().__init__(class_name)
        self.coords = coords
        self.start = start
        self.end = end

    def draw(self) -> Optional[BaseElement]:
        parameters = {
            'class_': self.class_name
        }
        if self.start:
            parameters['marker_start'] = f"url(#{self.class_name}-start)"
        if self.end:
            parameters['marker_end'] = f"url(#{self.class_name}-end)"
        return Polyline(points=[coord.center.point.coordinates for coord in self.coords], **parameters)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}], "
            f"{self.start!r}, "
            f"{self.end!r}"
            f")"
        )
