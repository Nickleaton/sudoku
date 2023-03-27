from typing import List, Tuple, Dict, Callable

from pulp import lpSum

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Killer(Region):

    def __init__(self, board, total: int, cells: List[Item]):
        super().__init__(board)
        self.total = total
        self.add_items(cells)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.total!r}, "
            f"{repr(self.cells)}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple[int, List[Item]]:
        parts = yaml[cls.__name__].split("=")
        total = int(parts[0].strip())
        cells = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in parts[1].split(',')]
        return total, cells

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        total, cells = Killer.extract(board, yaml)
        return Killer(board, total, cells)

    def glyphs(self, selector: Callable[[Item], bool]) -> List[Glyph]:
        # TODO
        return []

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                "Killer",
                1,
                "Numbers cannot repeat within cages. The cells total to the number in the top leftmost cell."
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Killer'})

    def add_constraint(self, solver: PulpSolver) -> None:
        total = lpSum(solver.values[cell.row][cell.column] for cell in self.cells)
        name = f"{self.__class__.__name__}_{self.cells[0].row}{self.cells[0].column}"
        solver.model += total == self.total, name

    def to_dict(self) -> Dict:
        cell_str = ",".join([f"{cell.row}{cell.column}" for cell in self.cells])
        return {self.__class__.__name__: f"{self.total}={cell_str}"}

    def css(self) -> Dict:
        return {
            '.Killer': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.KillerForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.KillerBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
