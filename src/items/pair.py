import abc
from typing import Optional, List, Set, Type, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.utils.rule import Rule


class Pair(Item):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board)
        self.c1 = c1
        self.c2 = c2

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r})"

    @property
    def used_classes(self) -> Set[Type[Item]]:
        result = {c for c in self.__class__.__mro__}.difference({abc.ABC, object})
        result = result.union(self.c1.used_classes)
        result = result.union(self.c2.used_classes)
        return result

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> 'Item':
        c1 = Cell(board, yaml[0][0], yaml[0][1])
        c2 = Cell(board, yaml[1][0], yaml[1][1])
        return cls(board, c1, c2)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Pair'})

    @property
    def difference(self) -> Optional[int]:
        return None

    @property
    def to_yaml(self):
        return repr([[self.c1.row, self.c1.column], [self.c2.row, self.c2.column]])
