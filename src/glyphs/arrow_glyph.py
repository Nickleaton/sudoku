"""ArrowGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class ArrowGlyph(Glyph):
    """Represents an arrow glyph to be drawn on an SVG canvas."""

    arrow = "\u2191"  # Define the arrow symbol (↑)

    def __init__(self, class_name: str, angle: float, position: Coord):
        """Initialize an ArrowGlyph instance.

        Create an arrow glyph with a specified class name, angle, and position.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            angle (float): The angle of the arrow in degrees.
            position (Coord): The position of the arrow, represented as a Coord object.

        Returns:
            None
        """
        super().__init__(class_name)
        self.angle = Angle(float(angle))  # Convert angle to an Angle object
        self.position = position

    def draw(self) -> BaseElement | None:
        """Draw the arrow on an SVG canvas.

        Create and return an SVG text element that represents the arrow, applying the specified
        position and rotation (angle) transformations.

        Returns:
            BaseElement: The SVG text element representing the arrow.
            None: If the element cannot be created.
        """
        # Create a text element for the arrow with the applied transformations
        text = Text("",
                    transform=self.position.transform + " " + self.angle.transform,
                    class_=self.class_name)
        # Create a span element for the arrow symbol itself
        span = TSpan(ArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return a string representation of the ArrowGlyph instance.

        This method provides a human-readable representation of the object, showing the class
        name, class_name, angle, and position.

        Returns:
            str: A string representation of the ArrowGlyph instance.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.angle.angle!r}, {self.position!r})"
