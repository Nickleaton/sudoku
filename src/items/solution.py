from itertools import product
from typing import List, Optional, Dict

from src.items.board import Board


class Solution:

    def __init__(self, board: Board, data: Optional[List[str]] = None):
        self.board = board
        if data is None:
            self.data = [[None for _ in board.column_range] for _ in board.row_range]
        else:
            self.data = [[int(data[row - 1][column - 1]) for column in board.column_range] for row in board.row_range]

    def set_value(self, row: int, column: int, value: int):
        self.data[row - 1][column - 1] = int(value)

    def get_value(self, row: int, column: int) -> int:
        return int(self.data[row - 1][column - 1])

    def __repr__(self) -> str:
        lines = [
            "".join([str(d) for d in self.data[row - 1]])
            for row in self.board.row_range
        ]
        return (f"Solution("
                f"{self.board!r},"
                f"{lines!r}"
                ")"
                )

    def __str__(self) -> str:
        result = "Solution:\n"
        for row in self.data:
            result += f"- {''.join([str(int(d)) for d in row])}\n"
        return result

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Solution):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self.get_value(row, column) != other.get_value(row, column):
                    return False
            return True
        raise Exception(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    @staticmethod
    def create(board: Board, yaml: Optional[Dict]) -> 'Solution':
        result = Solution(board)
        for row in board.row_range:
            line = str(yaml[row - 1])
            for column in board.column_range:
                value = line[column - 1]
                result.set_value(row, column, value)
        return result
