"""Bltr."""

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.cell import Cell
from src.items.standard_diagonal import StandardDiagonal
from src.utils.coord import Coord


class BLTR(StandardDiagonal):
    """Represents start bottom-left to top-right diagonal constraint on start Sudoku board."""

    def __init__(self, board: Board):
        """Initialize start BLTR diagonal constraint for the given board.

        Args:
            board (Board): The Sudoku board on which this diagonal operates.
        """
        super().__init__(board)
        self.add_items([Cell.make(board, board.maximum_digit - i + 1, i) for i in board.row_range])

    def glyphs(self) -> list[Glyph]:
        """Generate the visual representation (glyph) for the diagonal.

        Returns:
            list[Glyph]: A list containing the diagonal's glyph.
        """
        return [LineGlyph('Diagonal', Coord(self.board.maximum_digit + 1, 1), Coord(1, self.board.maximum_digit + 1))]
