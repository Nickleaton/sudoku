"""
Kropki Dots
"""
from itertools import product
from typing import List, Dict

from pulp import LpVariable, LpInteger, lpSum

from src.glyphs.glyph import Glyph, CircleGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class KropkiPair(Pair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        super().__init__(board, cell_1, cell_2)
        self.sos: Dict[int, LpVariable] = {}

    @property
    def factor(self) -> int:
        return 2

    @property
    def factor_name(self) -> str:
        return "double"

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"A black dot between two cells means that one of the digits in those cells "
                    f"is exactly {self.factor_name} the other"
                )
            )
        ]

    def glyphs(self, selector) -> List[Glyph]:
        return [CircleGlyph(self.__class__.__name__, self.cell_1.coord.center, self.cell_2.coord.center)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Kropki'})

    def valid(self, x: int, y: int) -> bool:
        """
        Does x and y conform to a possible multiple?
        :param x: first digit
        :param y: second digit
        :return: returns true if x is a multiple of self.factor and the same for y and x
        """
        return x == self.factor * y or self.factor * x == y

    def possible(self) -> set:
        """
        Work stubs which digits are possible
        :return: set of digits
        """
        used = set({})
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if self.valid(x, y):
                used.add(x)
                used.add(y)
        return used

    def add_impossible_constraint(self, solver: PulpSolver) -> None:
        """
        Set any impossible digits to not be a choice
        :param solver: solver
        """
        for digit in set(self.board.digit_range) - self.possible():
            name = f"{self.name}_Impossible_{digit}_{self.cell_1.row}_{self.cell_1.column}"
            solver.model += solver.choices[digit][self.cell_1.row][self.cell_1.column] == 0, name
            name = f"{self.name}_Impossible_{digit}_{self.cell_2.row}_{self.cell_2.column}"
            solver.model += solver.choices[digit][self.cell_2.row][self.cell_2.column] == 0, name

    def add_implausible_constraint(self, solver: PulpSolver) -> None:
        for x, y in product(self.board.digit_range, self.board.digit_range):
            choice1 = solver.choices[x][self.cell_1.row][self.cell_1.column]
            choice2 = solver.choices[y][self.cell_2.row][self.cell_2.column]
            if not self.valid(x, y):
                solver.model += choice1 + choice2 <= 1, f"{self.name}_Implausible_{x}_{y}"

    @property
    def count(self) -> int:
        count = 0
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if self.valid(x, y):
                count += 1
        return count

    def create_sos(self, solver: PulpSolver) -> None:
        sos_range = range(0, self.count)
        self.sos = LpVariable.dicts(self.name, sos_range, 0, 1, LpInteger)
        solver.model += lpSum([self.sos[i] for i in sos_range]) == 1, f"{self.name}_SOS"

    def add_unique_constraints(self, solver: PulpSolver) -> None:
        count = 0
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if not self.valid(x, y):
                continue
            choice1 = solver.choices[x][self.cell_1.row][self.cell_1.column]
            choice2 = solver.choices[y][self.cell_2.row][self.cell_2.column]
            solver.model += choice1 + choice2 + (1 - self.sos[count]) <= 2, f"{self.name}_Valid_{x}_{y}"
            count += 1

    def add_constraint(self, solver: PulpSolver) -> None:
        self.add_impossible_constraint(solver)
        self.add_implausible_constraint(solver)
        self.create_sos(solver)
        self.add_unique_constraints(solver)

    def css(self) -> Dict:
        return {
            '.KropkiPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black',
                'background': 'transparent'
            }
        }
