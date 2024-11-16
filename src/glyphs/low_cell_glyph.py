"""LowCellGlyph."""
from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LowCellGlyph(Glyph):
    """Represents a low cell glyph for SVG drawing.

    Inherits from Glyph and provides functionality to generate
    an SVG symbol for a low cell and to draw it using a specific
    coordinate.
    """

    def __init__(self, class_name: str, coord: Coord):
        """Initialize a LowCellGlyph instance.

        Args:
            class_name (str): The class name for the glyph.
            coord (Coord): The coordinate of the glyph.
        """
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Symbol]:
        """Create and return the SVG symbol for the low cell glyph.

        The symbol is represented by a circle with a radius of 35
        centered at (50, 50).

        Returns:
            Optional[Symbol]: The SVG symbol for the low cell glyph, or None.
        """
        result = Symbol(
            viewBox="0 0 100 100",
            id_="LowCell-symbol",
            class_="LowCell"
        )
        result.add(Circle(center=(50, 50), r=35))
        return result

    def draw(self) -> Optional[BaseElement]:
        """Draw the low cell glyph by using the defined symbol and coordinates.

        Returns:
            Optional[BaseElement]: The SVG use element that references the
            low cell symbol and positions it based on the coordinate.
        """
        return Use(href="#LowCell-symbol", insert=self.coord.point.coordinates, class_="LOwCell", height=100, width=100)

    def __repr__(self) -> str:
        """Return a string representation of the LowCellGlyph instance.

        Returns:
            str: The string representation of the LowCellGlyph.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.coord!r})"
