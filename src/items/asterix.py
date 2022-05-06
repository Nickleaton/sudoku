from typing import List, Any

from src.glyphs.glyph import Glyph, SquareGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Asterix(Region):
    coords = [
        Coord(2, 5),
        Coord(3, 3),
        Coord(3, 7),
        Coord(5, 2),
        Coord(5, 5),
        Coord(5, 8),
        Coord(7, 3),
        Coord(7, 7),
        Coord(8, 5)
    ]

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, int(coord.row), int(coord.column)) for coord in Asterix.coords])

    @classmethod
    def extract(cls, board: Board, yaml: Any) -> Any:
        return yaml

    @classmethod
    def create(cls, board: Board, yaml: Any) -> Item:
        return cls(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Window', 1, 'Digits cannot repeat in highlighted cells')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [SquareGlyph('Asterix', cell.coord, 1) for cell in self.cells]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Asterix'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)
