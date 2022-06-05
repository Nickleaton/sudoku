import re
from typing import Optional, List, Dict, Tuple, Callable

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.item import Item
from src.utils.rule import Rule


class PencilMarkCell(CellReference):

    def __init__(self, board: Board, row: int, column: int, digits: List[int]):
        super().__init__(board, row, column)
        self.digits = digits

    def svg(self) -> Optional[Glyph]:
        return None

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'PencilMark'})

    @property
    def rules(self) -> List[Rule]:
        return [Rule("PencilMark", 1, "Digits restricted")]

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        return []

    def css(self) -> Dict:
        return {
            ".PencilMarkCell": {
                "fill": "gainsboro"
            }
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r}, {repr(self.digits)})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.cell.row_column_string}={''.join([str(d) for d in self.digits])}"}

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        row_str, column_str, digits = match.groups()
        return int(row_str), int(column_str), [int(s) for s in digits]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        row, column, digits = cls.extract(board, yaml)
        return cls(board, row, column, digits)

    def bookkeeping(self) -> None:
        self.cell.book.set_possible(self.digits)
