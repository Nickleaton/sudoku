from typing import Optional, List, Dict, Callable

from src.glyphs.glyph import Glyph
from src.glyphs.mid_cell_glyph import MidCellGlyph
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class MidCell(CellReference):

    @staticmethod
    def digits() -> List[int]:
        return [4, 5, 6]

    @staticmethod
    def included(digit: int) -> bool:
        return digit in MidCell.digits()

    def letter(self) -> str:
        return 'm'

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Mid", 1, "The digits 4, 5 and 6 are marked with blue squares")]

    def glyphs(self) -> List[Glyph]:
        return [MidCellGlyph('MidCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        return {
            ".MidCell": {
                "stroke": "blue",
                "fill": "white"
            }
        }

    def bookkeeping(self) -> None:
        self.cell.book.set_possible(MidCell.digits())
