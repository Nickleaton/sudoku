from typing import List, Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class ThermometerGlyph(PolyLineGlyph):
    def __init__(self, class_name: str, coords: List[Coord]):
        super().__init__(class_name, coords, True, False)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="Thermometer-start",
            class_="Thermometer ThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
