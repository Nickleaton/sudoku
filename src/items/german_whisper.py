from typing import List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine


class GermanWhisper(GreaterThanEqualDifferenceLine):

    def __init__(self, board: Board, cells: List[Cell]):
        super().__init__(board, cells, 5)

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('GermanWhisper', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'German Whisper'})
