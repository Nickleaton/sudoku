import abc
import re
from typing import List, Set, Type, Tuple, Dict, Optional

from pulp import LpElement

from src.glyphs.glyph import Glyph, CircleGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord


class FixedPair(Pair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, total: int):
        super().__init__(board, cell_1, cell_2)
        self.total = total

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r}, {self.total})"

    @property
    def used_classes(self) -> Set[Type[Item]]:
        result = set(self.__class__.__mro__).difference({abc.ABC, object})
        result = result.union(self.cell_1.used_classes)
        result = result.union(self.cell_2.used_classes)
        return result

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        rc_pattern = f"[{board.digit_values}][{board.digit_values}]"
        int_pattern = "[1-9][0-9]*"
        regex = re.compile(f"({rc_pattern})-({rc_pattern})=({int_pattern})")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        c1_str, c2_str, total_str = match.groups()
        c1 = Cell.make(board, int(c1_str[0]), int(c1_str[1]))
        c2 = Cell.make(board, int(c2_str[0]), int(c2_str[1]))
        return c1, c2, total_str

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        c1, c2, total = cls.extract(board, yaml)
        return cls(board, c1, c2, total)

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Fixed Pair'})

    @property
    def label(self) -> str:
        return ""

    def glyphs(self, selector) -> List[Glyph]:
        return [
            CircleGlyph(
                self.__class__.__name__,
                Coord.middle(self.cell_1.coord.center, self.cell_2.coord.center),
                0.15
            )
        ]

    def to_dict(self) -> Dict:
        return {
            self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}={self.total}"
        }

    def target(self, solver: PulpSolver) -> Optional[LpElement]:
        return None

    def add_constraint(self, solver: PulpSolver) -> None:
        target = self.target(solver)
        if target is None:
            return
        solver.model += target == self.total, self.name
