from typing import List, Any, Dict

from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.composed import Composed
from src.items.even_cell import EvenCell
from src.items.fortress_cell import FortressCell
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.odd_cell import OddCell


class Knowns(Composed):

    def __init__(self, board: Board, rows: List[str]):
        super().__init__(board, [])
        self.rows = rows
        parts: List[CellReference] = []
        for y, data in enumerate(self.rows):
            row = y + 1
            for x, digit in enumerate(data):
                column = x + 1
                if digit == '.':
                    pass
                elif digit == 'e':
                    parts.append(EvenCell(board, row, column))
                elif digit == 'o':
                    parts.append(OddCell(board, row, column))
                elif digit == 'f':
                    parts.append(FortressCell(board, row, column))
                else:
                    parts.append(KnownCell(board, row, column, int(digit)))
        self.add_items(parts)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        return [list(str(y)) for y in yaml[cls.__name__]]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        items = Knowns.extract(board, yaml)
        return Knowns(board, items)

    def line_str(self) -> str:
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]

        for item in self:
            lines[item.row - 1][item.column - 1] = item.letter()
        return ["".join(line) for line in lines]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.line_str()})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: self.line_str()}
