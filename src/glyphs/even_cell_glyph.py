"""EvenCellGlyph."""

from svgwrite.base import BaseElement
from svgwrite.shapes import Rect

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class EvenCellGlyph(Glyph):
    """Represents an even cell glyph to be drawn with SVG, inheriting from the Glyph class."""

    def __init__(self, class_name: str, position: Coord):
        """Initialize the EvenCellGlyph with the given class name and position.

        Args:
            class_name (str): The class name for the SVG element.
            position (Coord): The position of the glyph in coordinates.
        """
        super().__init__(class_name)
        self.position = position  # The position of the glyph
        self.size = Coord(1, 1) * config.graphics.even_cell_percentage

    def draw(self) -> BaseElement | None:
        """Draw the glyph as an SVG rectangle with the appropriate position and size.

        Returns:
            BaseElement | None: An SVG BaseElement (start rectangle) or None if not drawn.
        """
        # Calculate the top-left corner of the rectangle after applying scaling
        top_left = self.position + Coord(1, 1) * config.graphics.even_cell_inset_percentage
        # Return an SVG rectangle element
        return Rect(transform=top_left.transform, size=self.size.point.coordinates, class_=self.class_name)

    def __repr__(self) -> str:
        """Return start string representation of the EvenCellGlyph.

        Returns:
            str: A string representing the EvenCellGlyph instance.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r})'
