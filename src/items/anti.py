from typing import List, Dict, Sequence, Any

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.utils.coord import Coord


class Anti(Composed):

    def __init__(self, board: Board, digits: List[int]):
        super().__init__(board, [])
        self.digits = digits
        for cell in Cell.cells():
            self.add_items(self.pairs(cell, digits))

    def offsets(self) -> List[Coord]:  # pylint: disable=no-self-use
        return []

    def pairs(self, c1: Cell, digits: List[int]) -> Sequence[DifferentPair]:
        result = []
        for offset in self.offsets():
            if not self.board.is_valid(int(c1.row + offset.row), int(c1.column + offset.column)):
                continue
            c2 = Cell.make(self.board, int(c1.row + offset.row), int(c1.column + offset.column))
            result.append(DifferentPair(self.board, c1, c2, digits))
        return result

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Chess', 'Anti'})

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        if not isinstance(yaml, list):
            return [f"Expecting a list, got {yaml!r}"]
        result = []
        for i in yaml:
            if not isinstance(i, int):
                result.append(f"Expecting int, got {i!r}")
            elif int(i) not in board.digit_range:
                result.append(f"Expecting digit, got {i!r}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        return list(yaml)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Anti.validate(board, yaml)
        lst = Anti.extract(board, yaml)
        return cls(board, lst)

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r}, {self.digits!r})"
