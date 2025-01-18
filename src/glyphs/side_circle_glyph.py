"""SideCircleGlyph."""

from src.glyphs.circle_glyph import CircleGlyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class SideCircleGlyph(CircleGlyph):
    """Represents a circular glyph that can be drawn on an SVG canvas."""

    def __init__(self, class_name: str, location1: Coord, location2: Coord, percentage: float) -> None:
        """Initialize the CircleGlyph instance.

        Args:
            class_name (str): CSS class name for styling the circle.
            location1 (Coord): Coordinate of first cell
            location2 (Coord): Coordinate of second cell
            percentage (float): Scale factor for the circle's radius relative to the cell size.

        Raises:
            ValueError: If the location1 and location 2 are not orthogonal.
        """
        if location1.row != location2.row and location1.column != location2.column:
            raise ValueError(f'Not orthogonal: {location1} and {location2}')
        super().__init__(class_name, percentage)
        self.location1: Coord = location1
        self.location2: Coord = location2
        self.position: Point = Point.create_from_coord(self.location1)

    @property
    def offset(self) -> Point:
        """Return the offset for the circle glyph.

        Returns:
            Point: The offset for the circle glyph.
        """
        size: float = config.graphics.cell_size / 2.0  # noqa: WPS432
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
