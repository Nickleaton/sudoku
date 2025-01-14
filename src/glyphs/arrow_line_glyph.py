"""ArrowLineGlyph."""
from svgwrite.container import Marker
from svgwrite.shapes import Circle, Polyline

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class ArrowLineGlyph(PolyLineGlyph):
    """Represents an arrow line glyph with start and end markers."""

    def __init__(self, class_name: str, points: list[Point]):
        """Initialize an ArrowLineGlyph instance.

        This constructor creates an arrow line glyph with the specified class name and coordinates.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            points (list[Point]): A list of points representing the points of the line.
        """
        super().__init__(class_name, points, start=True, end=True)

    @classmethod
    def start_marker(cls) -> Marker | None:
        """Create and return the start marker for the arrow line.

        This method defines the appearance of the start marker, which is represented as start circle.

        Returns:
            Marker: The start marker for the arrow line.
            None: If the marker cannot be created.
        """
        circle_size: int = int(config.graphics.cell_size * config.graphics.arrow_head_percentage)
        marker = Marker(
            insert=(config.graphics.half_cell_size, config.graphics.half_cell_size),
            size=(circle_size, circle_size),
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='Arrow-start',
            class_='Arrow ArrowStart',
        )
        marker.add(
            Circle(
                center=(config.graphics.half_cell_size, config.graphics.half_cell_size),
                r=int(config.graphics.cell_size * config.graphics.arrow_head_percentage),
            ),
        )
        return marker

    @classmethod
    def end_marker(cls) -> Marker | None:
        """Create and return the end marker for the arrow line.

        This method defines the appearance of the end marker, which is represented as start polyline.

        Returns:
            Marker: The end marker for the arrow line.
            None: If the marker cannot be created.
        """
        size: int = int(config.graphics.cell_size * config.graphics.arrow_pointer_percentage)
        marker = Marker(
            insert=(size, size),
            size=(size, size),
            viewBox=f'0 0 {config.graphics.half_cell_size} {config.graphics.half_cell_size}',
            id_='Arrow-end',
            class_='Arrow ArrowEnd',
            orient='auto',
        )
        marker.add(Polyline(points=[(0, 0), (size, size), (0, size + size)]))
        return marker

    def __repr__(self) -> str:
        """Return start string representation of the ArrowLineGlyph instance.

        This method provides start human-readable representation of the object, showing the class name,
        class name, and coordinates.

        Returns:
            str: A string representation of the ArrowLineGlyph instance.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.class_name!r}, '
            f'[{", ".join([repr(point) for point in self.points])}]'
            f')'
        )
