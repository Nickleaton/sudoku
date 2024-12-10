"""ArrowGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.angle import Angle
from src.utils.coord import Coord


class ArrowGlyph(Glyph):
    """Represents an arrow glyph to be drawn on an SVG canvas."""

    arrow: str = '\u2191'  # Define the arrow symbol (↑)

    def __init__(self, class_name: str, angle: float, position: Coord) -> None:
        """Initialize an ArrowGlyph instance.

        Args:
            class_name (str): The class name to be assigned to the SVG element.
            angle (float): The angle of the arrow in degrees.
            position (Coord): The position of the arrow, represented as a `Coord` object.
        """
        super().__init__(class_name)
        self.angle: Angle = Angle(angle)  # Convert angle to an `Angle` object.
        self.position: Coord = position

    def draw(self) -> BaseElement | None:
        """Draws the arrow on an SVG canvas.

        Creates and returns an SVG text element that represents the arrow, applying the specified
        position and rotation (angle) transformations.

        Returns:
            BaseElement | None: The SVG text element representing the arrow, or `None` if the
            element cannot be created.
        """
        # Combine transformations into a single formatted string.
        transform: str = f'{self.position.transform} {self.angle.transform}'

        # Create the text element for the arrow with the applied transformations.
        text: Text = Text(
            '',
            transform=transform,
            class_=self.class_name,
        )
        # Create the span element for the arrow symbol itself.
        span: TSpan = TSpan(
            ArrowGlyph.arrow,
            alignment_baseline='central',
            text_anchor='middle',
        )
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return a string representation of the ArrowGlyph instance.

        This method provides a human-readable representation of the object, showing the class
        name, class name, angle, and position.

        Returns:
            str: A string representation of the ArrowGlyph instance.
        """
        return (
            f'{self.__class__.__name__}'
            f'({self.class_name!r}, {self.angle.angle!r}, {self.position!r})'
        )
