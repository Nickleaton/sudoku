import abc
from typing import List, Set, Type, Any, Tuple, Dict

from src.glyphs.glyph import Glyph, EdgeTextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.utils.rule import Rule


class Pair(Item):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board)
        self.c1 = c1
        self.c2 = c2

    @property
    def name(self) -> str:
        return f"{self.__class__.__name__}_{self.c1.row}_{self.c1.column}_{self.c2.row}_{self.c2.column}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r})"

    @property
    def used_classes(self) -> Set[Type[Item]]:
        result = set(self.__class__.__mro__).difference({abc.ABC, object})
        result = result.union(self.c1.used_classes)
        result = result.union(self.c2.used_classes)
        return result

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Tuple:
        c1_str, c2_str = yaml[cls.__name__].split('-')
        c1 = Cell.make(board, int(c1_str[0]), int(c1_str[1]))
        c2 = Cell.make(board, int(c2_str[0]), int(c2_str[1]))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: Any) -> Item:
        c1, c2 = cls.extract(board, yaml)
        return cls(board, c1, c2)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Pair'})

    @property
    def label(self) -> str:
        return "XX"

    @property
    def glyphs(self) -> List[Glyph]:
        return [EdgeTextGlyph(self.__class__.__name__, 0, self.c1.coord.center, self.c2.coord.center, self.label)]

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.c1.rc}-{self.c2.rc}"}
