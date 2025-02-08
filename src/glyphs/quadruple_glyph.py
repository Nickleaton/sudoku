"""QuadrupleGlyph."""
from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.shapes import Circle
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class QuadrupleGlyph(Glyph):
    """Represents a quadruple glyph consisting of a circle and associated text in SVG format."""

    def __init__(self, class_name: str, position: Point, numbers: str) -> None:
        """Initialize the QuadrupleGlyph with class name, location, and numbers to display.

        Args:
            class_name (str): The class name for the SVG elements.
            position (Point): The location where the circle and text should be placed.
            numbers (str): The text to display inside the circle.
        """
        super().__init__(class_name)
        self.position: Point = position  # The location of the glyph
        self.numbers: str = numbers  # The numbers to be displayed inside the circle

    def draw(self) -> BaseElement:
        """Draw the circle and the associated text for the quadruple glyph.

        This method creates an SVG `Group` containing a `Circle` and a `Text` element.
        The circle is placed at the bottom-right of the location, and the numbers are
        rendered inside the circle.

        Returns:
            BaseElement: An SVG `Group` containing the circle and text elements, or None if unable to draw.
        """
        group: Group = Group()
        bottom_right: Point = Point(1, 1) * config.graphics.cell_size + self.position
        circle: Circle = Circle(
            class_=f'{self.class_name}Circle',
            center=bottom_right.coordinates,
            r=config.graphics.cell_size * config.graphics.quadruple.percentage / 2.0,
        )
        group.add(circle)

        # Create Text element with the numbers centered inside the circle
        text: Text = Text(class_=f'{self.class_name}Text', text='', transform=bottom_right.transform)
        span: TSpan = TSpan(self.numbers, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        group.add(text)

        return group

    @property
    def priority(self) -> int:
        """Returns the priority of the QuadrupleGlyph.

        This property defines the importance of the glyph when ordering or rendering.
        The higher the number, the higher the priority.

        Returns:
            int: The priority of the glyph, set to 20. (see config)
        """
        return int(config.graphics.quadruple.priority)

    def __repr__(self) -> str:
        """Return string representation of the QuadrupleGlyph.

        Returns:
            str: A string representing the QuadrupleGlyph instance, including its class name, location, and numbers.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r}, {self.numbers!r})'
