from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class LowCellGlyph(Glyph):
    """Represents a glyph for a low cell, rendered using an SVG symbol and circle."""

    def __init__(self, class_name: str, coord: Coord):
        """Initialize the LowCellGlyph with the given class name and coordinates.

        Args:
            class_name (str): The class name for the SVG element.
            coord (Coord): The coordinates where the glyph will be placed.
        """
        super().__init__(class_name)
        self.coord = coord  # Coordinates for the low cell glyph

    @classmethod
    def symbol(cls) -> Optional[Symbol]:
        """Create the SVG symbol for the low cell glyph, containing a circle.

        This method defines a symbol that can be reused in the SVG output. The symbol
        consists of a circle with a radius of 35 units, centered at (50, 50) within a 100x100 viewBox.

        Returns:
            Optional[Symbol]: An SVG symbol element representing the low cell glyph.
        """
        result = Symbol(
            viewBox="0 0 100 100",
            id_="LowCell-symbol",
            class_="LowCell"
        )
        result.add(Circle(center=(50, 50), r=35))  # Adding a circle inside the symbol
        return result

    def draw(self) -> Optional[BaseElement]:
        """Draw the LowCellGlyph by referencing the SVG symbol.

        This method uses the defined symbol and places it at the coordinates specified in `self.coord`.

        Returns:
            Optional[BaseElement]: An SVG Use element that references the symbol, positioned at `coord`.
        """
        return Use(href="#LowCell-symbol", insert=self.coord.point.coordinates, class_="LowCell", height=100, width=100)

    def __repr__(self) -> str:
        """Return a string representation of the LowCellGlyph.

        Returns:
            str: A string representing the LowCellGlyph instance with its class name and coordinates.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.coord!r})"
