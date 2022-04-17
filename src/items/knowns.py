from typing import List, Dict, Any

from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.composed import Composed
from src.items.even_cell import EvenCell
from src.items.fortress_cell import FortressCell
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.items.odd_cell import Odd


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
                    parts.append(Odd(board, row, column))
                elif digit == 'f':
                    parts.append(FortressCell(board, row, column))
                else:
                    parts.append(KnownCell(board, row, column, int(digit)))
        self.add_items(parts)

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        return [list(y) for y in yaml]

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Knowns.validate(board, yaml)
        items = Knowns.extract(board, yaml)
        return Knowns(board, items)

    def __repr__(self) -> str:
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]
        for item in self:
            lines[item.row - 1][item.column - 1] = item.letter()
        line_str = ["".join(line) for line in lines]
        return f"{self.__class__.__name__}({self.board!r}, {line_str})"
