from typing import List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_line import DifferenceLine


class DutchWhisper(DifferenceLine):

    def __init__(self, board: Board, cells: List[Cell]):
        super().__init__(board, cells)
        self.difference = 4

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('DutchWhisper', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Dutch Whisper'})
