"""CentreCircleGlyph."""

from src.glyphs.circle_glyph import CircleGlyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class CentreCircleGlyph(CircleGlyph):
    """Represents a circular glyph at the center of a cell that can be drawn on an SVG canvas."""

    def __init__(self, class_name: str, location: Coord, percentage: float) -> None:
        """Initialize the CircleGlyph instance.

        Args:
            class_name (str): CSS class name for styling the circle.
            location (Coord): The center location of the circle on the canvas.
            percentage (float): Scale factor for the circle's radius relative to the cell size.
        """
        super().__init__(class_name, percentage)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location)

    @property
    def offset(self) -> Point:
        """Return the offset for the circle glyph.

        Returns:
            Point: The offset for the circle glyph.
        """
        size: float = config.graphics.cell_size / 2.0  # noqa: WPS432
        return Point(size, size)

    def __repr__(self) -> str:
        """Return string representation of the CircleGlyph instance.

        Returns:
            str: A string representation of the CircleGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.percentage!r})"
