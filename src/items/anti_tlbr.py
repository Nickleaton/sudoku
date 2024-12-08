"""AntiTlbr."""
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.anti_diagonal import AntiDiagonal
from src.items.cell import Cell
from src.utils.coord import Coord


class AntiTLBR(AntiDiagonal):
    """Represents an AntiTLBR item on a board.

    TLBR = Top left to bottom right.

    Inherits from the AntiDiagonal class and adds specific functionality
    for the AntiTLBR, which includes managing cells on the anti-diagonal
    from the top-left to the bottom-right of the board.
    """

    def __init__(self, board: Board):
        """Initialize the AntiTLBR with a board.

        Args:
            board (Board): The board on which the AntiTLBR will be placed.
        """
        super().__init__(board)
        # Adds cells along the anti-diagonal from top-left to bottom-right
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    def glyphs(self) -> list[Glyph]:
        """Return the glyphs associated with the AntiTLBR.

        Glyphs visually represent the AntiTLBR's position on the board.

        Returns:
            list[Glyph]: A list of glyphs representing the AntiTLBR.
        """
        return [
            LineGlyph('Diagonal',
                      # Starting coordinate of the diagonal
                      Coord(1, 1),
                      # Ending coordinate of the diagonal
                      Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1)
                      )
        ]
