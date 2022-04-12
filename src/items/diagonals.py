from typing import List, Dict

from src.glyphs.glyph import Glyph, LineGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Diagonal(Region):

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> Item:
        return cls(board)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    @property
    def rules(self) -> List[Rule]:
        return [Rule('Diagonal', 1, "Digits along a blue diagonal cannot repeat")]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Diagonal', 'Uniqueness'})


class TLBR(Diagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        cells = [Cell.make(self, i, i) for i in board.row_range]
        self.add_items(cells)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> Item:
        return cls(board)

    @property
    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(1, 1), Coord(self.board.maximum_digit + 1, self.board.maximum_digit + 1))]

    @property
    def rules(self) -> List[Rule]:
        return [Rule('TLBR', 1, "Digits along a blue diagonal cannot repeat")]

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver, "TLBR")


class BLTR(Diagonal):

    def __init__(self, board: Board):
        super().__init__(board)
        cells = [Cell.make(self, board.maximum_digit - i + 1, i) for i in board.row_range]
        self.add_items(cells)

    @classmethod
    def create(cls, name: str, board: Board, yaml: Dict) -> Item:
        return cls(board)

    @property
    def glyphs(self) -> List[Glyph]:
        return [LineGlyph('Diagonal', Coord(self.board.maximum_digit + 1, 1), Coord(1, self.board.maximum_digit + 1))]

    @property
    def rules(self) -> List[Rule]:
        return [Rule('BLTR', 1, "Digits along a blue diagonal cannot repeat")]

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_unique_constraint(solver, "BLTR")
