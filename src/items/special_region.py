from typing import List, Dict

from src.glyphs.glyph import Glyph, SquareGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class SpecialRegion(Region):

    def __init__(self, board: Board):
        super().__init__(board)
        self.add_items([Cell.make(board, int(coord.row), int(coord.column)) for coord in self.coords()])

    # pylint: disable=no-self-use
    def region_name(self) -> str:
        return ""

    # pylint: disable=no-self-use
    def coords(self) -> List[Coord]:
        return []

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return cls(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule(self.region_name(), 1, 'Digits cannot repeat in highlighted cells')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [SquareGlyph(self.region_name(), cell.coord, 1) for cell in self.cells]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({self.region_name()})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}
