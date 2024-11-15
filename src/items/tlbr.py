"""Tlbr."""
from typing import List

from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.standard_diagonal import StandardDiagonal
from src.utils.coord import Coord


class TLBR(StandardDiagonal):
    """Represents a top-left to bottom-right diagonal constraint on a Sudoku board."""

    def __init__(self, board: Board):
        """Initialize a TLBR diagonal constraint for the given board.

        Args:
            board (Board): The Sudoku board on which this diagonal operates.
        """
        super().__init__(board)
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    def glyphs(self) -> List[Glyph]:
        """Generate the visual representation (glyph) for the diagonal.

        Returns:
            List[Glyph]: A list containing the diagonal's glyph.
        """
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]
