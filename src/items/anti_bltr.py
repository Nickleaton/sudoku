from typing import List, Callable

from src.glyphs.glyph import Glyph, LineGlyph
from src.items.anti_diagonal import AntiDiagonal
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.utils.coord import Coord


class AntiBLTR(AntiDiagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, board.maximum_digit - i + 1, i) for i in board.row_range])

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(self.board.maximum_digit + 1, 1), Coord(1, self.board.maximum_digit + 1))]
