"""LittleArrowGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.point import Point

config: Config = Config()


class LittleArrowGlyph(Glyph):
    """Represents a small arrow glyph, drawn using an SVG text element."""

    arrow: str = '\u25B2'  # Unicode character for an upward triangle (▲)

    def __init__(self, class_name: str, location: Coord, direction: int):
        """Initialize the LittleArrowGlyph with the given class name, location, and direction.

        Args:
            class_name (str): The class name for the SVG element.
            location (Coord): The grid coordinate of the glyph's location.
            direction (int): The direction of the arrow, represented as an angle in degrees.
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location)  # Converts Coord to Point
        self.direction: int = direction

    def draw(self) -> BaseElement:
        """Draw the arrow glyph as an SVG text element.

        Returns:
            BaseElement: An SVG Text element containing the arrow symbol, or None if not drawn.
        """
        direction: Coord = Moves.directions()[self.direction - 1]
        size: float = config.graphics.little_arrow.percentage * config.graphics.cell_size
        position: Point = self.position + Point(1, 1) * size  # Adjust by arrow size
        transform = f'{position.transform} {direction.angle.transform}'

        text: Text = Text('', transform=transform, class_=self.class_name)
        span: TSpan = TSpan(self.arrow, alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return a string representation of the LittleArrowGlyph.

        Returns:
            str: A string representing the instance with its class name, location, and direction.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r}, {self.direction!r})'
