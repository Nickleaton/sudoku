from itertools import product
from typing import List, Optional, Dict

from src.items.board import Board


class Answer:

    def __init__(self, board: Board, data: Optional[List[str]] = None):
        self.board = board
        self.data: List[List[int]] = [
            [0 for _ in board.column_range]
            for _ in board.row_range
        ]
        if data is not None:
            for row, column in product(board.row_range, board.column_range):
                digit = int(data[row - 1][column - 1])
                self.set_value(row, column, digit)

    def set_value(self, row: int, column: int, value: int) -> None:
        self.data[row - 1][column - 1] = value

    def get_value(self, row: int, column: int) -> int:
        return self.data[row - 1][column - 1]

    def __repr__(self) -> str:
        lines = [
            "".join([str(d) for d in self.data[row - 1]])
            for row in self.board.row_range
        ]
        return (f"Answer("
                f"{self.board!r},"
                f"{lines!r}"
                ")"
                )

    def __str__(self) -> str:
        result = "Answer:\n"
        for row in self.data:
            result += f"  - {''.join([str(int(d)) for d in row])}\n"
        return result

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Answer):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self.get_value(row, column) != other.get_value(row, column):
                    return False
            return True
        return other == self

    @classmethod
    def extract(cls, _: Board, yaml: Dict) -> List[str]:
        return [str(line) for line in yaml]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'Answer':
        return Answer(board, Answer.extract(board, yaml))

    def standard_string(self) -> str:

        def separator(self) -> str:
            result = ""
            for column in self.board.column_range:
                if (column - 1) % self.board.box_columns == 0:
                    result += "+-"
                result += "--"
            return result + "+\n"

        assert self.board.box_rows is not None
        result = ""
        for row in self.board.row_range:
            if (row - 1) % self.board.box_rows == 0:
                result += separator(self)
            for column in self.board.column_range:
                if (column - 1) % self.board.box_columns == 0:
                    result += "| "
                result += f"{self.data[row - 1][column - 1]} "
            result += "|\n"
        result += separator(self)
        return result
