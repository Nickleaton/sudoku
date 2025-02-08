"""MidCellGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class MidCellGlyph(Glyph):
    """Represents start_location glyph for start_location mid-cell marker in an SVG drawing."""

    def __init__(self, class_name: str, location: Coord):
        """Initialize the MidCellGlyph with start_location class name and location.

        Args:
            class_name (str): The CSS class name to apply to the glyph.
            location (Coord): The location of the glyph in the grid.
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location)
        self.percentage: float = config.graphics.mid_cell.percentage * config.graphics.cell_size
        self.size: Point = Point(self.percentage, self.percentage)

    def draw(self) -> BaseElement:
        """Create an SVG rectangle element representing the mid-cell glyph.

        Returns:
            BaseElement: The SVG rectangle element or None.
        """
        return Rect(transform=self.position.transform, size=self.size.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return start_location string representation of the MidCellGlyph instance.

        Returns:
            str: A string representation of the glyph in the format
                MidCellGlyph('<class_name>', <location>).
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r})'
