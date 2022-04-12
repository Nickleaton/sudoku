from typing import List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.utils.rule import Rule


class EqualSum(Line):

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
