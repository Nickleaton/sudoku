from typing import List, Dict, Any, Tuple

from pulp import lpSum

from src.glyphs.glyph import TextGlyph, Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.cyclic import Cyclic
from src.utils.rule import Rule
from src.utils.side import Side


class LittleKiller(Region):

    # pylint: disable=too-many-arguments
    def __init__(self, board: Board, side: Side, cyclic: Cyclic, offset: int, total: int):
        super().__init__(board)
        self.side = side
        self.cyclic = cyclic
        self.offset = offset
        self.total = total
        coord = side.start(board, cyclic, offset)
        delta = side.direction(cyclic).offset
        cells = []
        while board.is_valid_coordinate(coord):
            cells.append(Cell.make(board, int(coord.row), int(coord.column)))
            coord += delta
        self.add_items(cells)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.cyclic!r}, "
            f"{self.offset!r}, "
            f"{self.total!r}"
            f")"
        )

    @staticmethod
    def validate(board: Board, yaml: Any) -> List[str]:
        results = []
        if not isinstance(yaml, str):
            results.append(f"Expecting str, got {yaml!r}")
            return results
        if "=" not in yaml:
            results.append(f"Not expected format, got {yaml!r}")
        parts = yaml.split("=")
        if len(parts) != 2:
            results.append(f"Expected two parts, got {yaml!r}")
        return results

    @staticmethod
    def extract(board: Board, yaml: Any) -> Tuple[int, int, Cyclic, Side]:
        parts = yaml.split("=")
        total = int(parts[1])
        offset = int(parts[0][1])
        cyclic = Cyclic.create(parts[0][-1])
        side = Side.create(parts[0][0])
        return total, offset, cyclic, side

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict | List | str | int | None) -> Item:
        LittleKiller.validate(board, yaml)
        total, offset, cyclic, side = LittleKiller.extract(board, yaml)
        return LittleKiller(board, side, cyclic, offset, total)

    # @property
    # def glyphs(self) -> List[Glyph]:
    #     return [
    #         TextGlyph('Outside', 0, self.reference + Coord(0.5, 0.5), str(self.total))
    #     ]

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                "LittleKiller",
                1,
                "Clues outside the grid give the sum of the indicated diagonals, which may contain repeated digits"
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'LittleKiller', 'Killer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        solver.model += lpSum(solver.values[cell.row][cell.column] for cell in self.cells) == self.total, \
                        f"{self.__class__.__name__}_{self.side.value}{self.cyclic.value}{self.offset}"
