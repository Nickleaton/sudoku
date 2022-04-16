from typing import Dict, List, Set, Type, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.utils.rule import Rule


class CellReference(Item):

    def __init__(self, board: Board, row: int, column: int):
        super().__init__(board)
        self.cell = Cell.make(board, row, column)
        self.row = row
        self.column = column

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting dict, got {yaml!r}")
            return result
        if 'Row' not in yaml:
            result.append(f"Row:, got {yaml!r}")
            return result
        if 'Column' not in yaml:
            result.append(f"Column:, got {yaml!r}")
            return result
        if yaml['Row'] not in board.digit_range or yaml['Column'] not in board.digit_range:
            result.append(f"Expecting digit,digit, got {yaml!r}")
        return result

    @staticmethod
    def extract(_: Board, yaml: Any) -> Tuple[int, int]:
        return int(yaml['Row']), int(yaml['Column'])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        CellReference.validate(board, yaml)
        row, column = CellReference.extract(board, yaml)
        return cls(board, row, column)

    def letter(self) -> str:
        return '.'  # pragma: no cover

    @property
    def rules(self) -> List[Rule]:
        return []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell!r})"

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union(self.cell.used_classes)
        return result