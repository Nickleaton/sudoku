from typing import List, Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle, Polyline

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class ArrowLineGlyph(PolyLineGlyph):
    """Arrow Line Glyph
    """

    def __init__(self, class_name: str, coords: List[Coord]):
        super().__init__(class_name, coords, True, True)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox="0 0 100 100",
            id_="Arrow-start",
            class_="Arrow ArrowStart"
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    @classmethod
    def end_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(20, 20),
            size=(20, 20),
            viewBox="0 0 50 50",
            id_="Arrow-end",
            class_="Arrow ArrowEnd",
            orient="auto"
        )
        marker.add(Polyline(points=[(0, 0), (20, 20), (0, 40)]))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
