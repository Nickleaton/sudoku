from typing import List, Dict, Sequence

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.constraint_exception import ConstraintException
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.utils.coord import Coord


class Anti(Composed):

    def __init__(self, board: Board, digits: List[int]):
        super().__init__(board, [])
        self.digits = digits
        for cell in Cell.cells():
            self.add_items(self.pairs(cell, digits))

    def offsets(self) -> List[Coord]:
        raise NotImplementedError

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

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        return Anti(board, yaml)

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r}, {self.digits!r})"
