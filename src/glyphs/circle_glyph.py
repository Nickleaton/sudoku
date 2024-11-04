from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord


class CircleGlyph(Glyph):
    """Represents a circular glyph that can be drawn on an SVG canvas.

    Attributes:
        class_name (str): CSS class name for the SVG element.
        center (Coord): The center coordinate of the circle.
        percentage (float): Scale factor for the radius relative to cell size.
    """

    def __init__(self, class_name: str, center: Coord, percentage: float) -> None:
        """Initializes the CircleGlyph.

        Args:
            class_name (str): CSS class name for styling the circle.
            center (Coord): The center point of the circle.
            percentage (float): Scale factor for the circle's radius relative to cell size.
        """
        super().__init__(class_name)
        self.center: Coord = center
        self.percentage: float = percentage

    @property
    def priority(self) -> int:
        """Defines the drawing priority for the circle glyph.

        Returns:
            int: Priority level of the glyph, with a fixed value of 10.
        """
        return 10

    def draw(self) -> Optional[BaseElement]:
        """Draws the circle glyph on an SVG canvas.

        Returns:
            Optional[BaseElement]: An SVG circle element if drawing is possible, otherwise None.
        """
        cell_size: int = 100
        if config.drawing is not None and config.drawing.cell_size is not None:
            cell_size = int(config.drawing.cell_size)
        return Circle(
            transform=self.center.point.transform,
            r=self.percentage * cell_size,
            class_=self.class_name
        )

    def __repr__(self) -> str:
        """Provides a string representation of the CircleGlyph instance.

        Returns:
            str: A string representation of the CircleGlyph.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {repr(self.center)}, {repr(self.percentage)})"
