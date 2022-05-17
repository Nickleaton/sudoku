from typing import List

from src.glyphs.glyph import Glyph, LineGlyph
from src.items.anti_diagonal import AntiDiagonal
from src.items.board import Board
from src.items.cell import Cell
from src.utils.coord import Coord


class AntiTLBR(AntiDiagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    @property
    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]
