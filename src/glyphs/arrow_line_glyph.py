"""ArrowLineGlyph."""
from svgwrite.container import Marker
from svgwrite.shapes import Circle, Polyline

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class ArrowLineGlyph(PolyLineGlyph):
    """Represents an arrow line glyph with start and end markers."""

    def __init__(self, class_name: str, coords: list[Coord]):
        """Initialize an ArrowLineGlyph instance.

        This constructor creates an arrow line glyph with the specified class name and coordinates.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            coords (list[Coord]): A list of coordinates representing the points of the line.

        Returns:
            None
        """
        super().__init__(class_name, coords, True, True)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return the start marker for the arrow line.

        This method defines the appearance of the start marker, which is represented as a circle.

        Returns:
            Marker: The start marker for the arrow line.
            None: If the marker cannot be created.
        """
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
    def end_marker(cls) -> Marker | None:
        """Create and return the end marker for the arrow line.

        This method defines the appearance of the end marker, which is represented as a polyline.

        Returns:
            Marker: The end marker for the arrow line.
            None: If the marker cannot be created.
        """
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
        """Return a string representation of the ArrowLineGlyph instance.

        This method provides a human-readable representation of the object, showing the class name,
        class name, and coordinates.

        Returns:
            str: A string representation of the ArrowLineGlyph instance.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
