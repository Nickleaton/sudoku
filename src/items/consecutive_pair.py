from typing import List, Tuple, Dict

from src.glyphs.glyph import Glyph, ConsecutiveGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.utils.rule import Rule


class ConsecutivePair(LessThanEqualDifferencePair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        super().__init__(board, cell_1, cell_2, 1)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        defintion = yaml[cls.__name__]
        definition_string_1, definition_string_2 = defintion.split("-")

        c1 = Cell.make(board, int(definition_string_1[0]), int(definition_string_1[1]))
        c2 = Cell.make(board, int(definition_string_2[0]), int(definition_string_2[1]))
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
        return [ConsecutiveGlyph(self.__class__.__name__, self.cell_1.coord.center, self.cell_2.coord.center)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r})"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}"}

    def css(self) -> Dict:
        return {
            '.ConsecutivePair': {
                'fill': 'white',
                'stroke-width': 2,
                'stroke': 'black'
            }
        }
