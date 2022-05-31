import re
from typing import List, Tuple, Dict, Optional

from pulp import lpSum

from src.glyphs.glyph import Glyph, TextGlyph, ArrowGlyph
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
        self.direction = side.direction(cyclic)
        self.delta = self.direction.offset
        cells = []
        while board.is_valid_coordinate(coord):
            cells.append(Cell.make(board, int(coord.row), int(coord.column)))
            coord += self.delta
        self.add_items(cells)
        self.reference = side.start(board, cyclic, offset) - self.delta

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

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[int, int, Cyclic, Side]:
        parts = yaml[cls.__name__].split("=")
        total = int(parts[1])
        offset = int(parts[0][1])
        cyclic = Cyclic.create(parts[0][-1])
        side = Side.create(parts[0][0])
        return total, offset, cyclic, side

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        total, offset, cyclic, side = LittleKiller.extract(board, yaml)
        return LittleKiller(board, side, cyclic, offset, total)

    def glyphs(self) -> List[Glyph]:
        delta2 = Coord(0, 0)
        if self.side == Side.TOP:
            delta2 = Coord(0, 1)
        if self.side == Side.RIGHT:
            delta2 = Coord(0, 1)
        # print(self.reference, self.delta, self.reference + self.delta, self.direction, self.to_dict(), delta2)
        return [
            TextGlyph('LittleKiller', 0, self.reference + Coord(0.5, 0.5), str(self.total)),
            ArrowGlyph('LittleKiller', self.direction.angle.angle, self.reference + (self.delta * 0.90) + delta2)
        ]

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

    def add_constraint(self, solver: PulpSolver, include: Optional[re.Pattern], exclude: Optional[re.Pattern]) -> None:
        total = lpSum(solver.values[cell.row][cell.column] for cell in self.cells)
        name = f"{self.__class__.__name__}_{self.side.value}{self.offset}{self.cyclic.value}"
        solver.model += total == self.total, name

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.offset}{self.cyclic.value}={self.total}"}

    def css(self) -> Dict:
        return {
            '.LittleKiller': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.LittleKillerForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.LittleKillerBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            },
            '.LittleArrow': {
                'font-size': '20px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            }

        }
