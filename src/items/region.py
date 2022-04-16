from typing import Dict, List

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver

REGION_TOTALS = False


class Region(Composed):
    """ Collection of cells"""

    def __init__(self, board: Board) -> None:
        super().__init__(board, [])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_none(yaml)
        return cls(board)

    @property
    def cells(self) -> List[Cell]:
        return [item for item in self.items if isinstance(item, Cell)]

    def __in__(self, cell: Cell) -> bool:
        return cell in self.cells

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def add_unique_constraint(self, solver: PulpSolver, name, optional: bool = False):
        for digit in self.board.digit_range:
            total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in self.cells])
            if optional:
                solver.model += total <= 1, f"Unique_{name}_{digit}"
            else:
                solver.model += total == 1, f"Unique_{name}_{digit}"

    def add_total_constraint(self, solver: PulpSolver, total: int, name: str) -> None:
        if REGION_TOTALS:
            value = lpSum([solver.values[cell.row][cell.column] for cell in self.cells])
            solver.model += value == total, f"Total_{name}"
