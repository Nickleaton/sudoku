from typing import List, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.cell_reference import CellReference
from src.items.constraint_exception import ConstraintException
from src.items.known_cell import KnownCell
from src.items.fortress_cell import FortressCell
from src.items.even_cell import Odd, Even
from src.items.composed import Composed
from src.items.item import Item


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
                    parts.append(Even(board, row, column))
                elif digit == 'o':
                    parts.append(Odd(board, row, column))
                elif digit == 'f':
                    parts.append(FortressCell(board, row, column))
                else:
                    parts.append(KnownCell(board, row, column, int(digit)))
        self.add_items(parts)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, str):
            raise ConstraintException(f"Expecting str, got {yaml:r}")
        return Knowns(board, [list(y) for y in yaml])

    def __repr__(self) -> str:
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]
        for item in self:
            lines[item.row - 1][item.column - 1] = item.letter()
        line_str = ["".join(line) for line in lines]
        return f"{self.__class__.__name__}({self.board!r}, {line_str})"
