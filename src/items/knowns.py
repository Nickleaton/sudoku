from typing import List, Optional, Dict

from src.items.board import Board
from src.items.cell import Even, Odd, Fortress, Known, Cell
from src.items.composed import Composed
from src.items.item import Item


class Knowns(Composed):

    def __init__(self, board: Board, rows: List[str]):
        super().__init__(board, [])
        self.rows = rows
        parts = []
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
                    parts.append(Fortress(board, row, column))
                else:
                    parts.append(Known(self, row, column, digit))
        self.add_items(parts)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self) -> Cell:
        if self._n < len(self.items):
            result = self.items[self._n]
            self._n += 1
            return result
        self._n = 0
        raise StopIteration

    @classmethod
    def create(cls, name: str, board: Board, yaml: Optional[Dict]) -> Item:
        return Knowns(board, [list(y) for y in yaml])

    def __repr__(self):
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]
        for item in self:
            lines[item.row - 1][item.column - 1] = item.letter()
        line_str = ["".join(line) for line in lines]
        return f"{self.__class__.__name__}({self.board!r}, {line_str})"
