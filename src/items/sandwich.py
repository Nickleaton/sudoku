import re
from typing import Dict, Tuple, List, Set, Type, Optional

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph, TextGlyph
from src.items.board import Board
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.functions import Functions
from src.utils.rule import Rule
from src.utils.side import Side


class Sandwich(Item):

    def __init__(self, board: Board, side: Side, index: int, total: int):
        super().__init__(board)
        self.side = side
        self.index = index
        self.total = total
        self.position = side.marker(board, self.index) + Coord(0.5, 0.5)

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([0-9]+)")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        side, offset, total = cls.extract(board, yaml)
        return cls(board, side, offset, total)

    def glyphs(self) -> List[Glyph]:
        return [
            TextGlyph('Sandwich', 0, self.position, str(self.total)),
        ]

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Sandwich',
                1,
                (
                    'Clues outside of the grid give the sum of the digits sandwiched between the 1 and the 9 '
                    'in that row/column '
                )
            )
        ]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r}, {self.side!r}, {self.index}, {self.total})"

    @property
    def used_classes(self) -> Set[Type['Item']]:
        result = super().used_classes
        result = result.union([self.__class__])
        return result

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        return {
            ".SandwichForeground": {
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1,
                "fill": "black"
            },
            ".SandwichBackground": {
                "font-size": "30px",
                "stroke": "white",
                "stroke-width": 8,
                "fill": "white",
                "font-weight": "bolder"
            }
        }

    def add_constraint_row(self,
                           solver: PulpSolver,
                           include: Optional[re.Pattern],
                           exclude: Optional[re.Pattern]
                           ) -> None:
        # set up boolean for sandwich.
        # eg = 1 if 1 or 9 else 0
        bread = LpVariable.dict(
            f"Row_{self.index}",
            self.board.board_rows,
            0,
            Functions.triangular(self.board.maximum_digit),
            LpInteger
        )
        for column in self.board.board_columns:
            one = solver.choices[1][self.index][column]
            big = solver.choices[self.board.maximum_digit][self.index][column]
            solver.model += bread[column] == one + big, f"Bread_column_{self.index}_{column}"

    def add_constraint_column(self,
                              solver: PulpSolver,
                              include: Optional[re.Pattern],
                              exclude: Optional[re.Pattern]
                              ) -> None:
        # set up boolean for sandwich.
        # eg = 1 if 1 or 9 else 0
        bread = LpVariable.dict(
            f"Column_{self.index}",
            self.board.board_columns,
            0,
            Functions.triangular(self.board.maximum_digit),
            LpInteger
        )
        for row in self.board.board_rows:
            one = solver.choices[1][row][self.index]
            big = solver.choices[self.board.maximum_digit][row][self.index]
            solver.model += bread[row] == one + big, f"Bread_row_{row}_{self.index}"

    def add_constraint(self, solver: PulpSolver) -> None:
        if self.side.horizontal:
            self.add_constraint_row(solver, include, exclude)
        else:
            self.add_constraint_column(solver, include, exclude)
