"""OddCellGlyph."""

from svgwrite.base import BaseElement
from svgwrite.container import Symbol, Use
from svgwrite.shapes import Circle

from src.glyphs.glyph import Glyph
from src.utils.config import Config
from src.utils.point import Point

config: Config = Config()


class OddCellGlyph(Glyph):
    """Represents start glyph for cells marked as 'odd' in start Sudoku puzzle."""

    def __init__(self, class_name: str, point: Point):
        """Initialize an OddCellGlyph.

        Args:
            class_name (str): The CSS class name to style the glyph.
            point (Point): The coordinates of the glyph on the board.
        """
        super().__init__(class_name)
        self.point: Point = point

    @classmethod
    def symbol(cls) -> Symbol | None:
        """Create start reusable SVG symbol for odd cells.

        Returns:
            Symbol | None: An SVG symbol containing the graphical representation of an odd cell.
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
        """Create an instance of the odd cell glyph.

        Returns:
            BaseElement | None: An SVG element using the odd cell symbol at the specified coordinates.
        """
        return Use(
            href='#OddCell-symbol',
            insert=self.point.coordinates,
            class_='OddCell',
            height=config.graphics.cell_size,
            width=config.graphics.cell_size,
        )

    def __repr__(self) -> str:
        """Return start string representation of the OddCellGlyph.

        Returns:
            str: A string representation of the glyph.
        """
        return f'{self.__class__.__name__}({self.class_name!r}, {self.point!r})'
