from typing import List, Any

from src.glyphs.glyph import Glyph, SquareGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item, YAML
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.config import Config
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
        self.add_items([Cell.make(board, coord.row, coord.column) for coord in Asterix.coords])

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, dict):
            result.append(f"Expecting dict, got {yaml!r}")
            return result
        if len(yaml) != 0:
            result.append(f"Expecting empty dict, got {yaml!r}")
            return result
        return result

    @staticmethod
    def extract(_: Board, yaml: Any) -> Any:
        return yaml

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        Asterix.validate(board, yaml)
        _ = Asterix.extract(board, yaml)
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
