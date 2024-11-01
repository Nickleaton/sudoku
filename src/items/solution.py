from itertools import product
from typing import List, Any, Dict

from strictyaml import Seq, Optional

from src.items.board import Board
from src.items.cell_reference import CellReference
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.items.known_cell import KnownCell
from src.parsers.solution_parser import SolutionParser
from src.solvers.answer import Answer


class Solution(ComposedItem):

    def __init__(self, board: Board, rows: List[str]):
        super().__init__(board, [])
        self.rows = rows
        parts: List[CellReference] = []
        for y, data in enumerate(self.rows):
            row = y + 1
            for x, digit in enumerate(data):
                column = x + 1
                parts.append(KnownCell(board, row, column, int(digit), 'Verify'))
        self.add_items(parts)

    @classmethod
    def schema(cls) -> Dict:
        return {Optional("Solution"): Seq(SolutionParser())}

    def __hash__(self):
        return hash("Solution")

    def get_value(self, row: int, column: int) -> int:
        return int(self.rows[row - 1][column - 1])

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        return [list(str(y)) for y in yaml[cls.__name__]]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        items = Solution.extract(board, yaml)
        return Solution(board, items)

    def line_str(self) -> List[str]:
        lines = [['.' for _ in self.board.column_range] for _ in self.board.row_range]
        for item in self:
            lines[item.row - 1][item.column - 1] = item.letter()
        return ["".join(line) for line in lines]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.line_str()})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: self.line_str()}

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Answer) or isinstance(other, Solution):
            for row, column in product(self.board.row_range, self.board.column_range):
                if self.get_value(row, column) != other.get_value(row, column):
                    return False
            return True
        raise Exception(f"Cannot compare {self} {other} {other.__class__.__name__} with {self.__class__.__name__}")
