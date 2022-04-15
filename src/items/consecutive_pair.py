from typing import List, Dict

from src.glyphs.glyph import Glyph, ConsecutiveGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.constraint_exception import ConstraintException
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.utils.rule import Rule


class ConsecutivePair(LessThanEqualDifferencePair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2, 1)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        if not isinstance(yaml, list):
            raise ConstraintException(f"Expecting list, got {yaml!r}")
        c1 = Cell.make(board, yaml[0][0], yaml[0][1])
        c2 = Cell.make(board, yaml[1][0], yaml[1][1])
        return cls(board, c1, c2)

    @property
    def rules(self) -> List[Rule]:
        return [Rule("ConsecutivePair", 1, "Cells separated by a white dot must be consecutive")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Consecutive'})

    @property
    def glyphs(self) -> List[Glyph]:
        return [ConsecutiveGlyph(self.__class__.__name__, self.c1.coord.center, self.c2.coord.center)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r})"
