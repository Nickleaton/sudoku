"""BetweenLineGlyph."""
from typing import List, Optional

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class BetweenLineGlyph(PolyLineGlyph):
    """Represents a line glyph with start and end markers.

    This class creates a line with markers at both ends. The markers are circular and
    are used to visually indicate the start and end points of the line.
    """

    def __init__(self, class_name: str, coords: List[Coord]):
        """Initialize a BetweenLineGlyph instance.

        This constructor creates a line glyph with specified class name and coordinates.
        The line is drawn between the provided coordinates, with markers at both ends.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            coords (List[Coord]): The coordinates of the line, represented as a list of `Coord` objects.

        Returns:
            None
        """
        super().__init__(class_name, coords, True, True)

    @classmethod
    def start_marker(cls) -> Optional[Marker]:
        """Create and return the SVG marker for the start of the line.

        This method generates an SVG marker with a circular shape to represent the start
        point of the line.

        Returns:
            Marker: The SVG marker for the start of the line.
            None: If the marker cannot be created.
        """
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
        """Create and return the SVG marker for the end of the line.

        This method generates an SVG marker with a circular shape to represent the end
        point of the line.

        Returns:
            Marker: The SVG marker for the end of the line.
            None: If the marker cannot be created.
        """
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
        """Return a string representation of the BetweenLineGlyph instance.

        This method provides a human-readable representation of the object, showing the
        class name, class name, and the coordinates of the line.

        Returns:
            str: A string representation of the BetweenLineGlyph instance.
        """
        return (
            f"{self.__class__.__name__}"
            f"("
            f"'{self.class_name}', "
            f"[{', '.join([repr(coord) for coord in self.coords])}]"
            f")"
        )
