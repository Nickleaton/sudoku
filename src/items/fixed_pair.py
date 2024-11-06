from typing import List, Tuple, Dict, Optional

from pulp import LpElement

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.parsers.cell_pairs_parser import CellPairsParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class FixedPair(Pair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        super().__init__(board, cell_1, cell_2)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r})"

    @classmethod
    def is_sequence(cls) -> bool:
        """ Return True if this item is a sequence. """
        return True

    @classmethod
    def parser(cls) -> CellPairsParser:
        """ Return the parser for this item. """
        return CellPairsParser()

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        lhs: str = yaml[cls.__name__].split('=')[0]
        rhs: str = yaml[cls.__name__].split('=')[1]
        c1: Cell = Cell.make(board, int(lhs[0]), int(lhs[1]))
        c2: Cell = Cell.make(board, int(rhs[0]), int(rhs[1]))
        return c1, c2

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        c1, c2, total = cls.extract(board, yaml)
        return cls(board, c1, c2)

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Fixed Pair'})

    @property
    def label(self) -> str:
        return ""

    def glyphs(self) -> List[Glyph]:
        return [
            CircleGlyph(
                self.__class__.__name__,
                Coord.middle(self.cell_1.coord.center, self.cell_2.coord.center),
                0.15
            )
        ]

    def to_dict(self) -> Dict:
        return {
            self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}"
        }

    def target(self, solver: PulpSolver) -> Optional[LpElement]:
        return None

    def add_constraint(self, solver: PulpSolver) -> None:
        target = self.target(solver)
        if target is None:
            return
        # TODO
