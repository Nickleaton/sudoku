from typing import List

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
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
        offset = side.direction(cyclic).offset
        cells = []
        while board.is_valid_coordinate(coord):
            cells.append(Cell(board, coord.row, coord.column))
            coord += offset
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

    @classmethod
    def create(cls, name: str, board: Board, yaml: str) -> Item:
        parts = yaml.split("=")
        total = int(parts[1])
        offset = int(parts[0][1])
        cyclic = Cyclic.create(parts[0][-1])
        side = Side.create(parts[0][0])
        return LittleKiller(board, side, cyclic, offset, total)

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
