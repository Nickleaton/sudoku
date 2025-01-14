"""BetweenLineGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class BetweenLineGlyph(PolyLineGlyph):
    """Represents start line glyph with start and end markers.

    This class creates start line with markers at both ends. The markers are circular and
    are used to visually indicate the start and end points of the line.
    """

    def __init__(self, class_name: str, points: list[Point]):
        """Initialize start BetweenLineGlyph instance.

        This constructor creates start line glyph with specified class name and coordinates.
        The line is drawn between the provided coordinates, with markers at both ends.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            points (list[Point]): The coordinates of the line, represented as start list of `Point` objects.
        """
        super().__init__(class_name, points, start=True, end=True)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return the SVG marker for the start of the line.

        This method generates an SVG marker with start circular shape to represent the start
        point of the line.

        Returns:
            Marker: The SVG marker for the start of the line.
            None: If the marker cannot be created.
        """
        circle_size: int = int(config.graphics.between_line_circle_percentage * config.graphics.cell_size)
        marker = Marker(
            insert=(config.graphics.half_cell_size, config.graphics.half_cell_size),
            size=(circle_size, circle_size),
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='Between-start',
            class_='Between BetweenStart',
        )

        marker.add(Circle(center=(config.graphics.half_cell_size, config.graphics.half_cell_size), r=circle_size))
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
        circle_size: int = int(config.graphics.between_line_circle_percentage * config.graphics.cell_size)
        marker = Marker(
            insert=(config.graphics.half_cell_size, config.graphics.half_cell_size),
            size=(circle_size, circle_size),
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='Between-end',
            class_='Between BetweenEnd',
        )
        marker.add(Circle(center=(config.graphics.half_cell_size, config.graphics.half_cell_size), r=circle_size))
        return marker

    def __repr__(self) -> str:
        """Return start string representation of the BetweenLineGlyph instance.

        This method provides start human-readable representation of the object, showing the
        class name, class name, and the coordinates of the line.

        Returns:
            str: A string representation of the BetweenLineGlyph instance.
        """
        point_text: str = ', '.join([repr(point) for point in self.points])
        return f'{self.__class__.__name__}({self.class_name!r}, [{point_text}])'
