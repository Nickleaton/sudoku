from typing import Dict, List

from src.glyphs.glyph import Glyph, BoxGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Box(StandardRegion):

    def __init__(self, board: Board, index: int):
        super().__init__(board, index)
        self.position = self.start()
        self.add_items(
            [
                Cell.make(board, int(self.position.row + ro - 1), int(self.position.column + co - 1))
                for ro in range(1, board.box_rows + 1)
                for co in range(1, board.box_columns + 1)
            ]
        )

    def start(self) -> Coord:
        r = ((self.index - 1) * self.board.box_rows) % self.board.maximum_digit + 1
        c = ((self.index - 1) // self.board.box_columns) * self.board.box_columns + 1
        return Coord(r, c)

    @property
    def size(self) -> Coord:
        return Coord(self.board.box_rows, self.board.box_columns)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        StandardRegion.validate(board, yaml)
        index = StandardRegion.extract(board, yaml)
        return cls(board, index)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Box', 1, 'Digits in each box must be unique')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [BoxGlyph('Box', self.position, self.size)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Box'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver, f"Box_{self.index!r}")
