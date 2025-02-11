"""CircleGlyph."""

from abc import ABC

from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class CircleGlyph(Glyph, ABC):
    """Represents a circular glyph that can be drawn on an SVG canvas."""

    def __init__(self, class_name: str, percentage: float) -> None:
        """Initialize the CircleGlyph instance.

        Args:
            class_name (str): CSS class name for styling the circle.
            percentage (float): Scale factor for the circle's radius relative to the cell size.
        """
        super().__init__(class_name)
        self.percentage: float = percentage
        self.position: Point = Point(0, 0)

    @property
    def offset(self) -> Point:
        """Return the offset for the circle glyph.

        Returns:
            Point: The offset for the circle glyph.
        """
        return Point(0, 0)

    @property
    def priority(self) -> int:
        """Get the priority level for rendering the circle glyph.

        Returns:
            int: The priority level of the circle glyph, fixed at 10.
        """
        return 10

    def draw(self) -> Circle:
        """Draw the circle glyph on an SVG canvas.

        Returns:
            Circle: The SVG Circle element if valid, otherwise `None`.

        Raises:
            ValueError: If the cell size is invalid.
        """
        cell_size = int(config.graphics.cell_size)
        if cell_size <= 0:
            raise ValueError(f'Invalid cell size: {cell_size}')
        return Circle(
            transform=(self.position + self.offset).transform,
            r=self.percentage * cell_size,
            class_=self.class_name,
        )

    def __repr__(self) -> str:
        """Return string representation of the CircleGlyph instance.

        Returns:
            str: A string representation of the CircleGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.percentage!r})"
