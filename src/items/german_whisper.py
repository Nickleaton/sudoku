from typing import Optional, List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_line import DifferenceLine
from src.items.item import Item


class GermanWhisper(DifferenceLine):

    def __init__(self, board: Board, cells: List[Cell]):
        super().__init__(board, cells)
        self.difference = 5

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('GermanWhisper', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'German Whisper'})
