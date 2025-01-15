"""ArrowLineGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle, Polyline

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class ArrowLineGlyph(PolyLineGlyph):
    """Represents an arrow line glyph with start_location and end_location markers."""

    def __init__(self, class_name: str, coords: list[Coord]):
        """Initialize an ArrowLineGlyph instance.

        This constructor creates an arrow line glyph with the specified class name and coordinates.

        Args:
            class_name (str): The CSS class name to assign to the SVG element.
            coords (list[Coord]): A list of `Coord` objects representing the points of the line.
        """
        super().__init__(class_name, coords, start=True, end=True)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return the start marker for the arrow line.

        Define the appearance of the start marker, which is represented as a circular marker.

        Returns:
            Marker | None: The SVG marker element for the start.s.
        """
        circle_size: int = int(config.graphics.cell_size * config.graphics.arrow_head_percentage)
        marker = Marker(
            insert=(config.graphics.half_cell_size, config.graphics.half_cell_size),
            size=(circle_size, circle_size),
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='Arrow-start_location',
            class_='Arrow ArrowStart',
        )
        marker.add(
            Circle(
                center=(config.graphics.half_cell_size, config.graphics.half_cell_size),
                r=circle_size,
            ),
        )
        return marker

    @classmethod
    def end_marker(cls) -> Marker | None:
        """Create and return the end_location marker for the arrow line.

        Define the appearance of the end_location marker, which is represented as a triangular polyline.

        Returns:
            Marker | None: The SVG marker element for the end_location, or `None` if creation fails.
        """
        size: int = int(config.graphics.cell_size * config.graphics.arrow_pointer_percentage)
        marker = Marker(
            insert=(size, size),
            size=(size, size),
            viewBox=f'0 0 {config.graphics.half_cell_size} {config.graphics.half_cell_size}',
            id_='Arrow-end_location',
            class_='Arrow ArrowEnd',
            orient='auto',
        )
        marker.add(
            Polyline(points=[(0, 0), (size, size), (0, size * 2)]),
        )
        return marker

    def __repr__(self) -> str:
        """Return a string representation of the ArrowLineGlyph instance.

        Provides a human-readable representation of the object, showing the class name,
        CSS class name, and coordinates.

        Returns:
            str: A string representation of the ArrowLineGlyph instance.
        """
        coords_repr = ', '.join(repr(coord) for coord in self.coords)
        return f'{self.__class__.__name__}({self.class_name!r}, [{coords_repr}])'
