"""SideCircleGlyph."""

from src.glyphs.circle_glyph import CircleGlyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class SideCircleGlyph(CircleGlyph):
    """Represents a circular glyph that can be drawn on an SVG canvas."""

    def __init__(self, class_name: str, first_location: Coord, second_location: Coord, percentage: float) -> None:
        """Initialize the CircleGlyph instance.

        Args:
            class_name (str): CSS class name for styling the circle.
            first_location (Coord): Coordinate of first cell
            second_location (Coord): Coordinate of second cell
            percentage (float): Scale factor for the circle's radius relative to the cell size.

        Raises:
            ValueError: If the location1 and location 2 are not orthogonal.
        """
        if first_location.row != second_location.row and first_location.column != second_location.column:
            raise ValueError(f'Not orthogonal: {first_location} and {second_location}')
        super().__init__(class_name, percentage)
        self.location1: Coord = first_location
        self.location2: Coord = second_location
        self.position: Point = Point.create_from_coord(self.location1)

    @property
    def offset(self) -> Point:
        """Return the offset for the circle glyph.

        Returns:
            Point: The offset for the circle glyph.
        """
        size: float = config.graphics.cell_size / 2.0
        if self.location1.is_vertical(self.location2):
            return Point((self.location2.row - self.location1.row), 0) * size
        return Point(0, (self.location2.column - self.location1.column)) * size

    def __repr__(self) -> str:
        """Return string representation of the CircleGlyph instance.

        Returns:
            str: A string representation of the CircleGlyph instance.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.class_name!r}, '
            f'{self.location1!r}, '
            f'{self.location2!r}, '
            f'{self.percentage!r}'
            ')'
        )
