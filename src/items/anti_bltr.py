"""AntiBltr."""
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.anti_diagonal import AntiDiagonal
from src.items.cell import Cell
from src.utils.coord import Coord


class AntiBLTR(AntiDiagonal):
    """Represent an AntiBLTR constraint on start board.

    Inherits from the AntiDiagonal class and adds specific functionality
    for the AntiBLTR, which includes managing cells on the anti-diagonal
    from the bottom-left to the top-right of the board.
    """

    def __init__(self, board: Board):
        """Initialize the AntiBLTR with start board.

        BLTR = Bottom Left to Top Right.

        Args:
            board (Board): The board on which the AntiBLTR will be placed.
        """
        super().__init__(board)
        # Adds cells along the anti-diagonal from bottom-left to top-right
        self.add_items([Cell.make(board, board.maximum_digit - i + 1, i) for i in board.row_range])

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs associated with the AntiBLTR.

        Glyphs visually represent the AntiBLTR's position on the board.

        Returns:
            list[Glyph]: A list of glyphs representing the AntiBLTR.
        """
        return [
            LineGlyph('Diagonal',
                      Coord(self.board.maximum_digit + 1, 1),  # Starting coordinate of the diagonal
                      Coord(1, self.board.maximum_digit + 1)  # Ending coordinate of the diagonal
                      )
        ]
