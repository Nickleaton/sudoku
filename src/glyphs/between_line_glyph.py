from typing import List, Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class BetweenLineGlyph(PolyLineGlyph):
    """Between line glyph
    """

    def __init__(self, class_name: str, coords: List[Coord]):
        super().__init__(class_name, coords, True, True)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox="0 0 100 100",
            id_="Between-start",
            class_="Between BetweenStart"
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    @classmethod
    def end_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox="0 0 100 100",
            id_="Between-end",
            class_="Between BetweenEnd"
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
