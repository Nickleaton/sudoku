from typing import List, Set, Type, Tuple, Optional, Dict

from src.glyphs.glyph import Glyph
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

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        data = yaml[cls.__name__]
        data = str(data)
        return int(data[0]), int(data[1])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        row, column = cls.extract(board, yaml)
        return cls(board, row, column)

    def svg(self) -> Optional[Glyph]:
        return None

    def letter(self) -> str:  # pylint: disable=no-self-use
        return '.'

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

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: int(self.cell.rc)}
