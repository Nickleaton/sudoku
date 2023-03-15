from typing import List, Tuple, Dict

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class DifferencePair(Pair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, digits: List[int]):
        super().__init__(board, cell_1, cell_2)
        self.digits = digits

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r}, {self.digits!r})"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        cell_string, difference_string = yaml[cls.__name__].split("=")
        cell_string_1, cell_string_2 = cell_string.split("-")
        cell_1 = Cell.make(board, int(cell_string_1[0]), int(cell_string_1[1]))
        cell_2 = Cell.make(board, int(cell_string_2[0]), int(cell_string_2[1]))
        digits = [int(d) for d in difference_string.split(",")]
        return cell_1, cell_2, digits

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        cell_1, cell_2, digits = DifferencePair.extract(board, yaml)
        return cls(board, cell_1, cell_2, digits)

    @property
    def rules(self) -> List[Rule]:
        return []

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Different'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for digit in self.digits:
            name = (
                f"{self.__class__.__name__}"
                f"_"
                f"{digit}"
                f"_"
                f"{self.cell_1.row}"
                f"_"
                f"{self.cell_1.column}"
                f"_"
                f"{self.cell_2.row}"
                f"_"
                f"{self.cell_2.column}"
            )
            choice1 = solver.choices[int(digit)][self.cell_1.row][self.cell_1.column]
            choice2 = solver.choices[int(digit)][self.cell_2.row][self.cell_2.column]
            solver.model += choice1 + choice2 <= 1, name

    def to_dict(self) -> Dict:
        return {
            self.__class__.__name__:
                (
                    f"{self.cell_1.row_column_string}"
                    f"-"
                    f"{self.cell_2.row_column_string}"
                    f"="
                    f"{','.join([str(d) for d in self.digits])}"
                )
        }
