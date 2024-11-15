"""CircleGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph, config
from src.utils.coord import Coord


class CircleGlyph(Glyph):
    """Represents a circular glyph that can be drawn on an SVG canvas.

    This class allows you to create a circle glyph with customizable size and
    position on an SVG canvas. The size of the circle is determined relative
    to the cell size, with a configurable percentage for scaling.

    Attributes:
        class_name (str): CSS class name for the SVG element.
        center (Coord): The center coordinate of the circle.
        percentage (float): Scale factor for the radius relative to cell size.
    """

    def __init__(self, class_name: str, center: Coord, percentage: float) -> None:
        """Initialize the CircleGlyph instance.

        This constructor sets the class name, center point, and scaling percentage
        for the circle's radius. It calls the parent constructor for the CSS class.

        Args:
            class_name (str): CSS class name for styling the circle.
            center (Coord): The center point of the circle on the canvas.
            percentage (float): Scale factor for the circle's radius relative
                                 to the cell size.

        Returns:
            None
        """
        super().__init__(class_name)
        self.center: Coord = center
        self.percentage: float = percentage

    @property
    def priority(self) -> int:
        """Get the priority level for drawing the circle glyph.

        This property defines the priority for rendering the circle on the canvas.
        A higher value means the glyph will be drawn later in the stacking order.

        Returns:
            int: The drawing priority level of the circle glyph, fixed at 10.
        """
        return 10

    def draw(self) -> Optional[BaseElement]:
        """Draw the circle glyph on an SVG canvas.

        This method creates an SVG `Circle` element with the specified center and
        radius, scaled by the `percentage` relative to the current cell size.

        Returns:
            Optional[BaseElement]: The SVG `Circle` element if drawing is possible,
            otherwise `None` if no valid configuration is available.
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
        """Return a string representation of the CircleGlyph instance.

        This method provides a human-readable representation of the `CircleGlyph`
        object, showing the class name, class name, center position, and scaling
        percentage.

        Returns:
            str: A string representation of the CircleGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.center!r}, {self.percentage!r})"

