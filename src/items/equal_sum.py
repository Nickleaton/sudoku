from typing import Optional, List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.line import Line
from src.utils.rule import Rule


class EqualSum(Line):

    def __init__(self, board: Board, cells: Optional[List[Cell]]):
        super().__init__(board, cells)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'EqualSum',
                1,
                "For each line, digits on the line have an equal sum N within each 3x3 box it passes through. "
                "If a line passes through the same box more than once, "
                "each individual segment of such a line within that box sums to N separately"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('EqualSum', [cell.coord for cell in self.items], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'EqualSum', 'Sum'})
