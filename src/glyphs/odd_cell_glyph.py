"""OddCellGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.point import Point

config: Config = Config()


class OddCellGlyph(Glyph):
    """Represents the glyph for 'odd' cells in a Sudoku puzzle, typically used for marking cells with odd values."""

    def __init__(self, class_name: str, location: Coord):
        """Initialize an OddCellGlyph for representing an odd cell.

        Args:
            class_name (str): The CSS class name to style the glyph (e.g., for SVG styling).
            location (Coord): The coordinates (row and column) for the glyph on the board.
        """
        super().__init__(class_name)
        self.location: Coord = location
        self.position: Point = Point.create_from_coord(self.location)

    @classmethod
    def symbol(cls) -> Symbol | None:
        """Create a reusable SVG symbol for odd cells.

        The symbol consists of a circle with a radius based on the configuration.

        Returns:
            Symbol | None: An SVG symbol for the odd cell, or None if there is an error.
        """
        symbol: Symbol = Symbol(
            viewBox=f'0 0 {config.graphics.cell_size} {config.graphics.cell_size}',
            id_='OddCell-symbol',
            class_='OddCell',
        )
        symbol.add(
            Circle(
                center=(config.graphics.half_cell_size, config.graphics.half_cell_size),
                r=int(config.graphics.cell_size * config.graphics.parity_cell.odd.size / 2.0),  # noqa: WPS432
            ),
        )
        return symbol

    def draw(self) -> BaseElement | None:
        """Draw the odd cell glyph on the board using the pre-defined symbol.

        Returns:
            BaseElement | None: An SVG Use element that references the OddCell symbol at the specified position.
        """
        return Use(
            href='#OddCell-symbol',
            insert=self.position.coordinates,
            class_='OddCell',
            height=config.graphics.cell_size,
            width=config.graphics.cell_size,
        )

    def __repr__(self) -> str:
        """Return a string representation of the OddCellGlyph.

        Returns:
            str: A human-readable string representing the OddCellGlyph instance.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.location!r})'
