from typing import List, Dict, Tuple, Any

from src.glyphs.glyph import Glyph, ConsecutiveGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.less_than_equal_difference_pair import LessThanEqualDifferencePair
from src.utils.rule import Rule


class ConsecutivePair(LessThanEqualDifferencePair):

    def __init__(self, board: Board, c1: Cell, c2: Cell):
        super().__init__(board, c1, c2, 1)

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:  # pylint: disable=too-many-branches
        if not isinstance(yaml, list):
            return [f"Expecting list, got {yaml!r}"]
        if len(yaml) != 2:
            return [f"Expecting two coords, got {yaml!r}"]
        if len(yaml[0]) != 2:
            return [f"Expecting two coords, got {yaml!r}"]
        if len(yaml[1]) != 2:
            return [f"Expecting two coords, got {yaml!r}"]
        result = []
        if not isinstance(yaml[0][0], int):
            result.append(f"Expecting digit, got {yaml[0][0]!r}")
        if not isinstance(yaml[0][1], int):
            result.append(f"Expecting digit, got {yaml[0][1]!r}")
        if not isinstance(yaml[1][0], int):
            result.append(f"Expecting digit, got {yaml[1][0]!r}")
        if not isinstance(yaml[1][1], int):
            result.append(f"Expecting digit, got {yaml[1][1]!r}")
        if len(result) > 0:
            return result
        if int(yaml[0][0]) not in board.row_range:
            result.append(f"Expecting row, got {yaml[0][0]!r}")
        if int(yaml[0][1]) not in board.row_range:
            result.append(f"Expecting column, got {yaml[0][1]!r}")
        if int(yaml[1][0]) not in board.row_range:
            result.append(f"Expecting row, got {yaml[1][0]!r}")
        if int(yaml[1][1]) not in board.row_range:
            result.append(f"Expecting column, got {yaml[1][1]!r}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Tuple:
        c1 = Cell.make(board, yaml[0][0], yaml[0][1])
        c2 = Cell.make(board, yaml[1][0], yaml[1][1])
        return c1, c2

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        ConsecutivePair.validate(board, yaml)
        c1, c2 = ConsecutivePair.extract(board, yaml)
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
