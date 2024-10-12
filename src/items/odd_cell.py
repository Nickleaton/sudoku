from typing import Optional, List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.odd_cell_glyph import OddCellGlyph
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class OddCell(CellReference):

    @staticmethod
    def included(digit: int) -> bool:
        return digit % 2 == 1

    def svg(self) -> Optional[Glyph]:
        return None

    def letter(self) -> str:
        return 'o'

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Odd", 1, "An opaque grey circle must contain an odd digit")]

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        return [OddCellGlyph('OddCell', Coord(self.row, self.column))]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Parity'})

    def css(self) -> Dict:
        return {
            ".OddCell": {
                "fill": "gainsboro"
            }
        }

    def bookkeeping(self) -> None:
        self.cell.book.set_impossible([digit for digit in self.board.digit_range if not OddCell.included(digit)])
