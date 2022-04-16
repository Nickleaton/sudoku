from itertools import product
from typing import List, Optional, Any

from src.items.board import Board


class Solution:

    def __init__(self, board: Board, data: Optional[List[str]] = None):
        self.board = board
        self.data: List[List[int | None]] = [
            [None for _ in board.column_range]
            for _ in board.row_range
        ]
        if data is not None:
            for row, column in product(board.row_range, board.column_range):
                digit = int(data[row - 1][column - 1])
                self.set_value(row, column, digit)

    def set_value(self, row: int, column: int, value: int) -> None:
        self.data[row - 1][column - 1] = value

    def get_value(self, row: int, column: int) -> Optional[int]:
        return self.data[row - 1][column - 1]

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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Solution):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self.get_value(row, column) != other.get_value(row, column):
                    return False
            return True
        raise Exception(f"Cannot compare {object.__class__.__name__} with {self.__class__.__name__}")

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml!r}")
            return result
        if len(yaml) != max(board.row_range):
            result.append(f"Expecting {max(board.row_range)} rows, got {len(yaml)}")
            return result
        for i, row in enumerate(yaml):
            if len(row) != max(board.column_range):
                result.append(f"Expecting {max(board.column_range)} items on row {i}, got {len(row)} '{row}'")
            for d in row:
                if d not in board.digit_range:
                    result.append(f"Not a valid digit {d} in row {i}, '{row}'")
        return result

    @staticmethod
    def extract(_: Board, yaml: List[str]) -> List[str]:
        return yaml

    @staticmethod
    def create(board: Board, yaml: Any) -> 'Solution':
        return Solution(board, Solution.extract(board, yaml))
