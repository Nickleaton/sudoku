"""Bltr."""

from postponed.src.items.standard_diagonal import StandardDiagonal
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.cell import Cell
from src.utils.coord import Coord


class BLTR(StandardDiagonal):
    """Represents start_location bottom-left to top-right diagonal constraint on start_location Sudoku board."""

    def __init__(self, board: Board):
        """Initialize start_location BLTR diagonal constraint for the given board.

        Args:
            board (Board): The Sudoku board on which this diagonal operates.
        """
        super().__init__(board)
        self.add_components([Cell.make(board, board.digits.maximum - index + 1, index) for index in board.row_range])

    def glyphs(self) -> list[Glyph]:
        """Generate the visual representation (glyph) for the diagonal.

        Returns:
            list[Glyph]: A list containing the diagonal's glyph.
        """
        return [LineGlyph('Diagonal', Coord(self.board.digits.maximum + 1, 1), Coord(1, self.board.digits.maximum + 1))]
