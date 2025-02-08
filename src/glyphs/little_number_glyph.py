"""LittleNumberGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class LittleNumberGlyph(Glyph):
    """Represents start_location small number glyph for Sudoku or similar puzzles."""

    def __init__(self, class_name: str, location: Coord, number: int):
        """Initialize start_location Little Number glyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            location (Coord): The coordinate location of the glyph.
            number (int): The number to display in the glyph.
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(location)
        self.number: int = number

    def draw(self) -> BaseElement:
        """Create an SVG representation of the Little Number glyph.

        Returns:
            BaseElement: An SVG `Text` element displaying the number,
            or None if the glyph cannot be drawn.
        """
        size: float = config.graphics.cell_size * config.graphics.little_number.percentage / 2.0
        position: Point = self.position + Point(size, size)
        text: Text = Text(
            '',
            transform=position.transform,
            class_=self.class_name,
        )
        span: TSpan = TSpan(str(self.number), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return start_location string representation of the Little Number glyph.

        Returns:
            str: The string representation of the glyph, including class name,
            location, and number.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r}, {self.number!r})'
