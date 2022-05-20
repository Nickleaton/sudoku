import re
from typing import List, Any, Dict

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Knight(ComposedItem):

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
    def tags(self) -> set[str]:
        return super().tags.union({'Knight'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        return [int(d) for d in yaml[cls.__name__].split(",")]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        digits = Knight.extract(board, yaml)
        return Knight(board, digits)

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule("Knight", 1,
                 f"Every digit in {self.digits!r} must see at least one identical digit via a knights move")
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        for digit in self.digits:
            for cell in self.cells:
                include = []
                for offset in self.offsets():
                    if self.board.is_valid_coordinate(cell.coord + offset):
                        include.append(cell.coord + offset)
                start = solver.choices[digit][cell.row][cell.column]
                possibles = lpSum([solver.choices[digit][i.row][i.column] for i in include])
                solver.model += start <= possibles, f"{self.name}_{cell.row}_{cell.column}_{digit}"

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: ", ".join([str(d) for d in self.digits])}
