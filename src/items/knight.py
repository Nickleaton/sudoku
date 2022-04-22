from typing import List, Any

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed import Composed
from src.items.item import Item, YAML
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Knight(Composed):

    def __init__(self, board: Board, digits: List[int]):
        super().__init__(board, [])
        self.add_items([Cell.make(board, row, column) for row in board.row_range for column in board.column_range])
        self.digits = digits

    @staticmethod
    def offsets() -> List[Coord]:
        return \
            [
                Coord(-1, -2),
                Coord(1, -2),
                Coord(-2, -1),
                Coord(-2, 1),
                Coord(-1, 2),
                Coord(1, 2),
                Coord(2, 1),
                Coord(2, -1)
            ]

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Knight'})

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml!r}")
            return result
        for digit in yaml:
            if digit not in board.digit_range:
                result.append(f"{digit} is not a valid digit")
        return result

    @staticmethod
    def extract(board: Board, yaml: Any) -> Any:
        return yaml

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        Knight.validate(board, yaml)
        digits = Knight.extract(board, yaml)
        return Knight(board, digits)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("Knight", 1,
                 f"Every digit in {self.digits!r} must see at least one identical digit via a knights move")
        ]

    def __repr__(self) -> str:
        return f"{self.name}({self.board!r}, {self.digits!r})"

    def add_constraint(self, solver: PulpSolver) -> None:
        for digit in self.digits:
            for cell in self.cells:
                include = []
                for offset in self.offsets():
                    if self.board.is_valid_coordinate(cell.coord + offset):
                        include.append(cell.coord + offset)
                start = solver.choices[digit][cell.row][cell.column]
                possibles = lpSum([solver.choices[digit][i.row][i.column] for i in include])
                solver.model += start <= possibles, f"{self.name}_{cell.row}_{cell.column}_{digit}"
