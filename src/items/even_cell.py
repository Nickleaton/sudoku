from typing import Optional, List, Dict

from src.glyphs.glyph import Glyph, EvenCellGlyph
from src.items.cell_reference import CellReference
from src.utils.coord import Coord
from src.utils.rule import Rule


class EvenCell(CellReference):

    @staticmethod
    def included(digit: int) -> bool:
        return digit % 2 == 0

    def letter(self) -> str:
        return 'e'

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Parity'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "An opaque grey square must contain an even digit")]

    @property
    def glyphs(self) -> List[Glyph]:
        return [EvenCellGlyph('EvenCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        return {
            ".EvenCell": {
                "fill": "gainsboro"
            }
        }

    def bookkeeping(self) -> None:
        for digit in self.board.digit_range:
            if EvenCell.included(digit):
                self.cell.set_possible([digit])
            else:
                self.cell.set_impossible([digit])
