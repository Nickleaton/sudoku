from typing import List, Sequence, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.greater_than_equal_difference_line import GreaterThanEqualDifferenceLine
from src.items.item import Item
from src.utils.rule import Rule


class GermanWhisper(GreaterThanEqualDifferenceLine):

    def __init__(self, board: Board, cells: Sequence[Cell]):
        super().__init__(board, cells, 5)
        self.excluded = [5]

    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('GermanWhisper', [cell.coord for cell in self.cells], False, False)]

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                "Any two cells directly connected by a green line must have a difference of at least 5"
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'German Whisper'})

    def css(self) -> Dict:
        return {
            '.GermanWhisper': {
                'stroke': 'green',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }
