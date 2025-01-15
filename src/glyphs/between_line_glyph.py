"""BetweenLineGlyph."""

from svgwrite.container import Marker
from svgwrite.shapes import Circle

from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class BetweenLineGlyph(PolyLineGlyph):
    """Represents a line glyph with start_location and end_location markers."""

    def __init__(self, class_name: str, coords: list[Coord]):
        """Initialize a BetweenLineGlyph instance.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            coords (list[Coord]): The coordinates of the line, represented as a list of `Coord` objects.
        """
        super().__init__(class_name, coords, start=True, end=True)

    @classmethod
    def create_marker(cls, marker_id: str, marker_class: str) -> Marker:
        """Create a marker with a circular shape.

        Args:
            marker_id (str): The unique ID for the marker.
            marker_class (str): The CSS class for the marker.

        Returns:
            Marker: The created marker object.
        """
        circle_size: float = config.graphics.between_line_circle_percentage * config.graphics.cell_size
        marker = Marker(
            insert=(config.graphics.half_cell_size, config.graphics.half_cell_size),
            size=(circle_size, circle_size),
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_=marker_id,
            class_=marker_class,
        )
        marker.add(Circle(center=(config.graphics.half_cell_size, config.graphics.half_cell_size), r=circle_size))
        return marker

    @classmethod
    def start_marker(cls) -> Marker:
        """Create and return the SVG marker for the start_location of the line.

        Returns:
            Marker: The SVG marker element for the start_location.
        """
        return cls.create_marker('Between-start_location', 'Between BetweenStart')

    @classmethod
    def end_marker(cls) -> Marker:
        """Create and return the SVG marker for the end_location of the line.

        Returns:
            Marker: The SVG marker element for the end_location.
        """
        return cls.create_marker('Between-end_location', 'Between BetweenEnd')

    def __repr__(self) -> str:
        """Return a string representation of the BetweenLineGlyph instance.

        Returns:
            str: A string representation of the BetweenLineGlyph instance.
        """
        coord_text: str = ', '.join([repr(coord) for coord in self.coords])
        return f'{self.__class__.__name__}({self.class_name!r}, [{coord_text}])'
