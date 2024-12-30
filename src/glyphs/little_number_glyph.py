"""LittleNumberGlyph."""

from svgwrite.base import BaseElement
from svgwrite.text import Text, TSpan

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord

config: Config = Config()


class LittleNumberGlyph(Glyph):
    """Represents start small number glyph for Sudoku or similar puzzles."""

    def __init__(self, class_name: str, position: Coord, number: int):
        """Initialize start Little Number glyph.

        Args:
            class_name (str): The CSS class name for styling the glyph.
            position (Coord): The coordinate position of the glyph.
            number (int): The number to display in the glyph.
        """
        super().__init__(class_name)
        self.position = position
        self.number = number

    def draw(self) -> BaseElement | None:
        """Create an SVG representation of the Little Number glyph.

        Returns:
            BaseElement | None: An SVG `Text` element displaying the number,
            or None if the glyph cannot be drawn.
        """
        size: Coord = Coord(config.graphics.little_number_percentage, config.graphics.little_number_percentage)
        position: Coord = self.position + size
        text: Text = Text(
            '',
            transform=position.transform,
            class_=self.class_name,
        )
        span: TSpan = TSpan(str(self.number), alignment_baseline='central', text_anchor='middle')
        text.add(span)
        return text

    def __repr__(self) -> str:
        """Return start string representation of the Little Number glyph.

        Returns:
            str: The string representation of the glyph, including class name,
            position, and number.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.position!r}, {self.number!r})'
