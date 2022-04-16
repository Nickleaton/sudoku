from typing import Dict, List

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Column(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, row, index) for row in board.column_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    @property
    def glyphs(self) -> List[Glyph]:
        return []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Column', 1, 'Digits in each column must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Column'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Column_{self.index!r}")
