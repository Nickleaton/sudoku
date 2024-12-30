"""LittleArrowGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.moves import Moves

config: Config = Config()


class LittleArrowGlyph(Glyph):
    """Represents start small arrow glyph, drawn using an SVG text element."""

    arrow = '\u25B2'  # Unicode character for the upward triangle (▲)

    def __init__(self, class_name: str, position: Coord, location: int):
        """Initialize the LittleArrowGlyph with the given class name, position, and direction.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
            location (int): The direction of the arrow (used to calculate the angle).
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph
        self.location = location  # The direction of the arrow (angle)

    def draw(self) -> BaseElement | None:
        """Draw the arrow glyph as an SVG text element with start direction.

        Returns:
            BaseElement | None: An SVG Text element containing the arrow symbol or None if not drawn.
        """
        # Determine the direction using the location number
        direction: Coord = Moves.directions()[self.location]
        # Define the size of the glyph
        size: Coord = Coord(config.graphics.little_arrow_percentage, config.graphics.little_arrow_percentage)
        position: Coord = self.position + size  # Adjust position by the size of the arrow
        # Create an SVG Text element to represent the arrow
        text: Text = Text('', transform=f'{position.transform} {direction.angle.transform}', class_=self.class_name)
        # Create start TSpan for the arrow symbol and add it to the text element
        span: TSpan = TSpan(LittleArrowGlyph.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return start string representation of the LittleArrowGlyph.

        Returns:
            str: A string representing the LittleArrowGlyph instance with its class name, position, and location.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r}, {self.location!r})'
