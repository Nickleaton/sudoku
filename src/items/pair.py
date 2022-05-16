import abc
from typing import List, Set, Type, Tuple, Dict

from src.glyphs.glyph import Glyph, EdgeTextGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.utils.rule import Rule


class Pair(Region):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        super().__init__(board)
        self.cell_1 = cell_1
        self.cell_2 = cell_2
        self.add(cell_1)
        self.add(cell_2)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r})"

    @property
    def used_classes(self) -> Set[Type[Item]]:
        result = set(self.__class__.__mro__).difference({abc.ABC, object})
        result = result.union(self.cell_1.used_classes)
        result = result.union(self.cell_2.used_classes)
        return result

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        c1_str, c2_str = yaml[cls.__name__].split('-')
        c1 = Cell.make(board, int(c1_str[0]), int(c1_str[1]))
        c2 = Cell.make(board, int(c2_str[0]), int(c2_str[1]))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
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
        return [
            EdgeTextGlyph(self.__class__.__name__, 0, self.cell_1.coord.center, self.cell_2.coord.center, self.label)
        ]

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}"}
