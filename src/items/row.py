from typing import Dict, List

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Row(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.add_items([Cell.make(board, index, row) for row in board.row_range])

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        Item.check_yaml_int(yaml)
        return cls(board, yaml)

    @property
    def glyphs(self) -> List[Glyph]:
        result = []
        for item in self.items:
            result.extend(item.glyphs)
        return result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Row', 1, 'Digits in each row must be unique')]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Row'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum, self.name)
        self.add_unique_constraint(solver, f"Row_{self.index!r}")
