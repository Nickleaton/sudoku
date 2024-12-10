"""QuadrupleGlyph."""
from svgwrite.base import BaseElement
from svgwrite.container import Group
from svgwrite.shapes import Circle
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class QuadrupleGlyph(Glyph):
    """Represents a quadruple glyph consisting of a circle and associated text in SVG format."""

    def __init__(self, class_name: str, position: Coord, numbers: str) -> None:
        """Initialize the QuadrupleGlyph with class name, position, and numbers to display.

        Args:
            class_name (str): The class name for the SVG elements.
            position (Coord): The position where the circle and text should be placed.
            numbers (str): The text to display inside the circle.
        """
        super().__init__(class_name)
        self.position: Coord = position  # The position of the glyph
        self.numbers: str = numbers  # The numbers to be displayed inside the circle

    def draw(self) -> BaseElement | None:
        """Draw the circle and the associated text for the quadruple glyph.

        This method creates an SVG `Group` containing a `Circle` and a `Text` element.
        The circle is placed at the bottom-right of the position, and the numbers are
        rendered inside the circle.

        Returns:
            BaseElement | None: An SVG `Group` containing the circle and text elements, or None if unable to draw.
        """
        group: Group = Group()

        # Create circle at the bottom-right of the position with a radius of 35
        circle: Circle = Circle(
            class_=f'{self.class_name}Circle',
            center=self.position.bottom_right.point.coordinates,
            r=35,
        )
        group.add(circle)

        # Create Text element with the numbers centered inside the circle
        text: Text = Text(class_=f'{self.class_name}Text', text='', transform=self.position.bottom_right.transform)
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
            int: The priority of the glyph, set to 20.
        """
        return 20

    def __repr__(self) -> str:
        """Return string representation of the QuadrupleGlyph.

        Returns:
            str: A string representing the QuadrupleGlyph instance, including its class name, position, and numbers.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r}, {self.numbers!r})'
