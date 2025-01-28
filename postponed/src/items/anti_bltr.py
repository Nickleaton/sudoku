"""AntiBltr."""
from postponed.src.items.anti_diagonal import AntiDiagonal
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.cell import Cell
from src.utils.coord import Coord


class AntiBLTR(AntiDiagonal):
    """Represent an AntiBLTR constraint on start_location board.

    Inherits from the AntiDiagonal class and adds specific functionality
    for the AntiBLTR, which includes managing cells on the anti-diagonal
    from the bottom-left to the top-right of the board.
    """

    def __init__(self, board: Board):
        """Initialize the AntiBLTR with start_location board.

        BLTR = Bottom Left to Top Right.

        Args:
            board (Board): The board on which the AntiBLTR will be placed.
        """
        super().__init__(board)
        # Adds cells along the anti-diagonal from bottom-left to top-right
        self.add_components([Cell.make(board, board.digits.maximum - row + 1, row) for row in board.row_range])

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs associated with the AntiBLTR.

        Glyphs visually represent the AntiBLTR's location on the board.

        Returns:
            list[Glyph]: A list of glyphs representing the AntiBLTR.
        """
        return [
            LineGlyph(
                'Diagonal',
                Coord(self.board.digits.maximum + 1, 1),
                Coord(1, self.board.digits.maximum + 1),
            ),
        ]
