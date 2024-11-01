from typing import List, Dict

from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class UniqueRegion(Region):

    def __init__(self, board, cells: List[Item]):
        super().__init__(board)
        self.add_items(cells)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{repr(self.cells)}"
            f")"
        )

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> List[Item]:
        cells = [Cell.make(board, int(rc.strip()[0]), int(rc.strip()[1])) for rc in yaml['UniqueRegion'].split(',')]
        return cells

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        cells = UniqueRegion.extract(board, yaml)
        return UniqueRegion(board, cells)

    def glyphs(self) -> List[Glyph]:
        # TODO
        return []

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                "UniqueRegion",
                1,
                "Numbers cannot repeat within the Unique Region."
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'UniqueRegion'})

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver)

    def to_dict(self) -> Dict:
        cell_str = ",".join([f"{cell.row}{cell.column}" for cell in self.cells])
        return {self.__class__.__name__: f"{cell_str}"}

    def css(self) -> Dict:
        return {
            '.UniqueRegion': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 2,
                'fill': 'black'
            },
            '.UniqueRegionForeground': {
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
                'fill': 'black'
            },
            '.UniqueRegionBackground': {
                'font-size': '30px',
                'stroke': 'white',
                'stroke-width': 8,
                'fill': 'white',
                'font-weight': 'bolder'
            }
        }
