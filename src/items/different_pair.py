from typing import List, Dict, Any, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class DifferentPair(Pair):

    def __init__(self, board: Board, c1: Cell, c2: Cell, digits: List[int]):
        super().__init__(board, c1, c2)
        self.digits = digits

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting dict, got {yaml!r}")
            return result
        if len(yaml) != 3:
            result.append(f"Expecting two cells, plus digits got {yaml!r}")
            return result
        if 'Digits' not in yaml:
            result.append(f"Expecting Digits:, got {yaml!r}")
        if 'Cells' not in yaml:
            result.append(f"Expecting Cells:, got {yaml!r}")
        if len(result) > 0:
            return result
        if len(yaml['Cells']) != 2:
            result.append(f"Expecting two Cells:, got {yaml!r}")
        if len(result) > 0:
            return result
        result.extend(Coord.validate(yaml['Cells'][0]))
        result.extend(Coord.validate(yaml['Cells'][1]))
        for digit in yaml['Digits']:
            if digit not in board.digit_range:
                result.extend(f"Invalid digit {digit}")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Tuple[Cell,Cell, List[int]]:
        c1 = Cell.make(board, yaml['Cells'][0][0], yaml['Cells'][0][1])
        c2 = Cell.make(board, yaml['Cells'][1][0], yaml['Cells'][1][1])
        digits = yaml['Digits']
        return c1, c2, digits

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        DifferentPair.validate(board, yaml)
        c1, c2, digits = DifferentPair.extract(board, yaml)
        return cls(board, c1, c2, digits)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Different'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for digit in self.digits:
            name = f"{self.__class__.__name__}_{digit}_{self.c1.row}_{self.c1.column}_{self.c2.row}_{self.c2.column}"
            choice1 = solver.choices[int(digit)][self.c1.row][self.c1.column]
            choice2 = solver.choices[int(digit)][self.c2.row][self.c2.column]
            solver.model += choice1 + choice2 <= 1, name
