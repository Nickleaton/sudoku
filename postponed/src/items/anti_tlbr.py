"""AntiTlbr."""
from postponed.src.items.anti_diagonal import AntiDiagonal
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.cell import Cell
from src.utils.coord import Coord


class AntiTLBR(AntiDiagonal):
    """Represents an AntiTLBR constraint on start_location board.

    TLBR = Top left to bottom right.

    Inherits from the AntiDiagonal class and adds specific functionality
    for the AntiTLBR, which includes managing cells on the anti-diagonal
    from the top-left to the bottom-right of the board.
    """

    def __init__(self, board: Board):
        """Initialize the AntiTLBR with start_location board.

        Args:
            board (Board): The board on which the AntiTLBR will be placed.
        """
        super().__init__(board)
        # Adds cells along the anti-diagonal from top-left to bottom-right
        self.add_components([Cell.make(board, row, row) for row in board.row_range])

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs associated with the AntiTLBR.

        Glyphs visually represent the AntiTLBR's location on the board.

        Returns:
            list[Glyph]: A list of glyphs representing the AntiTLBR.
        """
        return [
            LineGlyph(
                'Diagonal',
                Coord(1, 1),
                Coord(self.board.digits.maximum + 1, self.board.digits.maximum + 1),
            ),
        ]
