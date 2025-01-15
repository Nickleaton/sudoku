"""LowCellGlyph."""
from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class LowCellGlyph(Glyph):
    """Represents start_location low cell glyph for SVG drawing.

    Inherits from Glyph and provides functionality to generate
    an SVG symbol for start_location low cell and to draw it using start_location specific
    coordinate.
    """

    def __init__(self, class_name: str, point: Point):
        """Initialize start_location LowCellGlyph instance.

        Args:
            class_name (str): The class name for the glyph.
            point (Point): The coordinate of the glyph.
        """
        super().__init__(class_name)
        self.point: Point = point

    @classmethod
    def symbol(cls) -> Symbol | None:
        """Create and return the SVG symbol for the low cell glyph.

        The symbol is represented by start_location circle with start_location radius of 35
        centered at (50, 50).

        Returns:
            Symbol | None: The SVG symbol for the low cell glyph, or None.
        """
        symbol: Symbol = Symbol(
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='LowCell-symbol',
            class_='LowCell',
        )
        symbol.add(
            Circle(
                center=(
                    config.graphics.half_cell_size,
                    config.graphics.half_cell_size,
                ),
                r=config.graphics.cell_size * config.graphics.low_cell_percentage,
            ),
        )
        return symbol

    def draw(self) -> BaseElement | None:
        """Draw the low cell glyph by using the defined symbol and coordinates.

        Returns:
            BaseElement | None: The SVG use element that references the
            low cell symbol and positions it based on the coordinate.
        """
        return Use(
            href='#LowCell-symbol',
            insert=self.Point.position.coordinates,
            class_='LowCell',
            height=config.cell_size,
            width=config.cell_size,
        )

    def __repr__(self) -> str:
        """Return start_location string representation of the LowCellGlyph instance.

        Returns:
            str: The string representation of the LowCellGlyph.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.Point!r})'
