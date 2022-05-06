from typing import List, Tuple, Dict

from src.glyphs.glyph import Glyph, ConsecutiveGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.utils.rule import Rule


class ConsecutivePair(LessThanEqualDifferencePair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2, 1)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        cs = yaml[cls.__name__]
        c1s, c2s = cs.split("-")
        c1 = Cell.make(board, int(c1s[0]), int(c1s[1]))
        c2 = Cell.make(board, int(c2s[0]), int(c2s[1]))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        c1, c2 = cls.extract(board, yaml)
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

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.c1.rc}-{self.c2.rc}"}
