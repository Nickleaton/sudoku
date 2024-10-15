from typing import Optional, List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.low_cell_glyph import LowCellGlyph
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class LowCell(CellReference):

    @staticmethod
    def digits() -> List[int]:
        return [1, 2, 3]

    @staticmethod
    def included(digit: int) -> bool:
        return digit in LowCell.digits()

    def letter(self) -> str:
        return 'l'

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Low", 1, "The digits 1,2 and 3 are marked with orange circles")]

    def glyphs(self) -> List[Glyph]:
        return [LowCellGlyph('LowCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        return {
            ".LowCell": {
                "stroke": "orange",
                "fill": "white"
            }
        }

    def bookkeeping(self) -> None:
        self.cell.book.set_possible(LowCell.digits())
