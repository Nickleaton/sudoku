from typing import List, Callable

from src.glyphs.glyph import Glyph, LineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_diagonal import StandardDiagonal
from src.utils.coord import Coord


class TLBR(StandardDiagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, i, i) for i in board.row_range])

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]
