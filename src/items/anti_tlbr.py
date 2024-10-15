from typing import List, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.line_glyph import LineGlyph
from src.items.anti_diagonal import AntiDiagonal
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.utils.coord import Coord


class AntiTLBR(AntiDiagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]
