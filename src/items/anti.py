from typing import List, Sequence, Any, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.different_pair import DifferentPair
from src.items.item import Item
from src.utils.coord import Coord


class Anti(ComposedItem):

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

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        return [int(part) for part in yaml[cls.__name__].split(', ')]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        lst = cls.extract(board, yaml)
        return cls(board, lst)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: ", ".join([str(d) for d in self.digits])}
