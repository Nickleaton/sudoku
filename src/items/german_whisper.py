from typing import List, Sequence, Dict

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.box import Box
from src.items.cell import Cell
from src.items.column import Column
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.row import Row


class GermanWhisper(GreaterThanEqualDifferenceLine):

    def __init__(self, board: Board, cells: Sequence[Cell]):
        super().__init__(board, cells, 5)
        self.excluded = [5]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('GermanWhisper', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'German Whisper'})

    def css(self) -> Dict:
        return {
            '.GermanWhisper': {
                'stroke': 'blue',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }

