from typing import Optional

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.coord import Coord


class OddCellGlyph(Glyph):
    """Represents a glyph for cells marked as 'odd' in a Sudoku puzzle."""

    def __init__(self, class_name: str, coord: Coord):
        """Initialize an OddCellGlyph.

        Args:
            class_name (str): The CSS class name to style the glyph.
            coord (Coord): The coordinates of the glyph on the board.
        """
        super().__init__(class_name)
        self.coord = coord

    @classmethod
    def symbol(cls) -> Optional[Symbol]:
        """Create a reusable SVG symbol for odd cells.

        Returns:
            Optional[Symbol]: An SVG symbol containing the graphical representation of an odd cell.
        """
        result = Symbol(
            viewBox="0 0 100 100",
            id_="OddCell-symbol",
            class_="OddCell"
        )
        result.add(Circle(center=(50, 50), r=35))
        return result

    def draw(self) -> Optional[BaseElement]:
        """Create an instance of the odd cell glyph.

        Returns:
            Optional[BaseElement]: An SVG element using the odd cell symbol at the specified coordinates.
        """
        return Use(
            href="#OddCell-symbol",
            insert=self.coord.point.coordinates,
            class_="OddCell",
            height=100,
            width=100
        )

    def __repr__(self) -> str:
        """Return a string representation of the OddCellGlyph.

        Returns:
            str: A string representation of the glyph.
        """
        return f"{self.__class__.__name__}('{self.class_name}', {self.coord!r})"
