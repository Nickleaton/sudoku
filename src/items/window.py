from typing import List, Any

from src.glyphs.glyph import Glyph, SquareGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item, YAML
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Window(Region):
    offsets = [
        Coord(-1, -1),
        Coord(-1, 0),
        Coord(-1, 1),
        Coord(0, -1),
        Coord(0, 0),
        Coord(0, 1),
        Coord(1, -1),
        Coord(1, 0),
        Coord(1, 1)
    ]

    def __init__(self, board: Board, center: Coord):
        super().__init__(board)
        self.center = center
        self.add_items(
            [
                Cell.make(board, int((center + offset).row), int((center + offset).column))
                for offset in Window.offsets
            ]
        )

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        result: List[str] = []
        if not isinstance(yaml, list):
            result.append(f"Expecting list, got {yaml!r}")
            return result
        if len(yaml) != 2:
            result.append(f"Expecting digit,digit, got {yaml!r}")
            return result
        if yaml[0] not in board.digit_range or yaml[1] not in board.digit_range:
            result.append(f"Expecting string digit,digit, got {yaml!r}")
        return result

    @staticmethod
    def extract(_: Board, yaml: Any) -> Coord:
        parts = yaml.split(",")
        return Coord(int(parts[0]), int(parts[1]))

    @classmethod
    def create(cls, name: str, board: Board, yaml: YAML) -> Item:
        Window.validate(board, yaml)
        coord: Coord = Window.extract(board, yaml)
        return cls(board, coord)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.center!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Window', 1, 'Digits in same shaded window must be unique')]

    @property
    def glyphs(self) -> List[Glyph]:
        return [SquareGlyph('Window', self.center - Coord(1, 1), 3)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Window'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)
