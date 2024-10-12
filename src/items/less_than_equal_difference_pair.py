from typing import Dict, Tuple

from src.items.board import Board
from src.items.cell import Cell
from src.items.difference_pair import DifferencePair
from src.solvers.pulp_solver import PulpSolver


class LessThanEqualDifferencePair(DifferencePair):

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'LessThanEqualDifference'})

    def add_constraint(self, solver: PulpSolver) -> None:
        value1 = solver.values[self.cell_1.row][self.cell_1.column]
        value2 = solver.values[self.cell_2.row][self.cell_2.column]
        difference = value1 - value2
        solver.model += difference <= self.difference, f"{self.name}_upper"
        solver.model += -difference <= self.difference, f"{self.name}_lower"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        cell_string, difference_string = yaml[cls.__name__]
        cell_string_1, cell_string_2 = cell_string.split("-")
        cell_1 = Cell.make(board, int(cell_string_1[0]), int(cell_string_1[1]))
        cell_2 = Cell.make(board, int(cell_string_2[0]), int(cell_string_2[1]))
        digits = [int(d) for d in difference_string.split(",")]
        return cell_1, cell_2, digits

    @property
    def difference(self) -> int:
        return 0
