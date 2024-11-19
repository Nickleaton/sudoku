"""ThermometerGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class ThermometerGlyph(PolyLineGlyph):
    """A thermometer-like glyph that represents a polyline with a start marker."""

    def __init__(self, class_name: str, coords: list[Coord]):
        """Initialize the ThermometerGlyph.

        Args:
            class_name (str): The CSS class name for styling the thermometer glyph.
            coords (list[Coord]): The list of coordinates defining the polyline.
        """
        super().__init__(class_name, coords, True, False)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Generate the start marker for the thermometer glyph.

        Returns:
            Marker | None: A Marker element representing the start of the thermometer.
        """
        marker = Marker(
            insert=(50, 50),
            viewBox="0 0 100 100",
            id_="Thermometer-start",
            class_="Thermometer ThermometerStart"
        )
        marker.add(Circle(center=(50, 50), r=30))
        return marker

    def __repr__(self) -> str:
        """Return a string representation of the ThermometerGlyph.

        Returns:
            str: A string representing the ThermometerGlyph with its class name and coordinates.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
