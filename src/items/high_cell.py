from typing import Optional, List, Dict, Callable

# from src.glyphs.glyph import Glyph, HighCellGlyph
from src.glyphs.glyph import Glyph
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.rule import Rule


class HighCell(CellReference):

    @staticmethod
    def digits() -> List[int]:
        return [7, 8, 9]

    @staticmethod
    def included(digit: int) -> bool:
        return digit in HighCell.digits()

    def letter(self) -> str:
        return 'h'

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Trio'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("Low", 1, "The digits 7, 8 and 9 are not marked")]

    def glyphs(self) -> List[Glyph]:
        return []
        # return [HighCellGlyph('HighCell', Coord(self.row, self.column))]

    def css(self) -> Dict:
        return {}

    def bookkeeping(self) -> None:
        self.cell.book.set_possible(HighCell.digits())
