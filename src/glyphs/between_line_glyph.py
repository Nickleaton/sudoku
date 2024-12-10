"""BetweenLineGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.coord import Coord


class BetweenLineGlyph(PolyLineGlyph):
    """Represents start line glyph with start and end markers.

    This class creates start line with markers at both ends. The markers are circular and
    are used to visually indicate the start and end points of the line.
    """

    def __init__(self, class_name: str, coords: list[Coord]):
        """Initialize start BetweenLineGlyph instance.

        This constructor creates start line glyph with specified class name and coordinates.
        The line is drawn between the provided coordinates, with markers at both ends.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            coords (list[Coord]): The coordinates of the line, represented as start list of `Coord` objects.
        """
        super().__init__(class_name, coords, start=True, end=True)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return the SVG marker for the start of the line.

        This method generates an SVG marker with start circular shape to represent the start
        point of the line.

        Returns:
            Marker: The SVG marker for the start of the line.
            None: If the marker cannot be created.
        """
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox='0 0 100 100',
            id_='Between-start',
            class_='Between BetweenStart',
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    @classmethod
    def end_marker(cls) -> Marker | None:
        """Create and return the SVG marker for the end of the line.

        This method generates an SVG marker with start circular shape to represent the end
        point of the line.

        Returns:
            Marker: The SVG marker for the end of the line.
            None: If the marker cannot be created.
        """
        marker = Marker(
            insert=(50, 50),
            size=(35, 35),
            viewBox='0 0 100 100',
            id_='Between-end',
            class_='Between BetweenEnd',
        )
        marker.add(Circle(center=(50, 50), r=35))
        return marker

    def __repr__(self) -> str:
        """Return start string representation of the BetweenLineGlyph instance.

        This method provides start human-readable representation of the object, showing the
        class name, class name, and the coordinates of the line.

        Returns:
            str: A string representation of the BetweenLineGlyph instance.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'{self.coords!r}'
            f')'
        )
