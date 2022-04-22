from typing import List, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item, YAML
from src.items.pair import Pair
from src.utils.coord import Coord
from src.utils.rule import Rule


class DifferencePair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell, difference: int):
        super().__init__(board, c1, c2)
        self.difference = difference

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting dict, got {yaml!r}")
            return result
        if len(yaml) != 2:
            result.append(f"Expecting two cells, plus difference {yaml!r}")
            return result
        if 'Cells' not in yaml:
            result.append(f"Expecting Cells:, got {yaml!r}")
        if 'Difference' not in yaml:
            result.append(f"Expecting Difference:, got {yaml!r}")
        if len(result) > 0:
            return result
        if len(yaml['Cells']) != 2:
            result.append(f"Expecting two Cells:, got {yaml!r}")
        if len(result) > 0:
            return result
        result.extend(Coord.validate(yaml['Cells'][0]))
        result.extend(Coord.validate(yaml['Cells'][1]))
        if yaml['Difference'] not in board.digit_range:
            result.append(f"Invalid digit {yaml['Difference']}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Tuple:
        c1 = Cell.make(board, yaml['Cells'][0][0], yaml['Cells'][0][1])
        c2 = Cell.make(board, yaml['Cells'][1][0], yaml['Cells'][1][1])
        difference: int = yaml['Difference']
        return c1, c2, difference

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        DifferencePair.validate(board, yaml)
        c1, c2, difference = DifferencePair.extract(board, yaml)
        return cls(board, c1, c2, difference)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference'})

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.c1!r}, {self.c2!r}, {self.difference!r})"
