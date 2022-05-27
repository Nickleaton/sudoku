"""
Kropki Dots
"""
import re
from itertools import product
from math import log10
from typing import List, Dict

from pulp import LpVariable, LpInteger, lpSum, LpContinuous

from src.glyphs.glyph import Glyph, KropkiGlyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.pair import Pair
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ProductPair(Pair):

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, ratio: int):
        super().__init__(board, cell_1, cell_2)
        self.ratio = ratio

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"A black dot between two cells means that one of the digits in those cells "
                    f"is exactly {self.ratio} times the other"
                )
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [KropkiGlyph(self.__class__.__name__, self.cell_1.coord.center, self.cell_2.coord.center)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'product'})

    def valid(self, x: int, y: int) -> bool:
        """
        Does x and y conform to a possible multiple?
        :param x: first digit
        :param y: second digit
        :return: returns true if x is a multiple of self.factor and the same for y and x
        """
        return x == self.ratio * y or self.ratio * x == y

    def possible(self) -> List[int]:
        """
        Work stubs which digits are possible
        :return: list of digits
        """
        result = []
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if self.valid(x, y):
                if x not in result:
                    result.append(x)
                if y not in result:
                    result.append(y)
        return result

    def bookkeeping(self) -> None:
        return
        self.cell_1.set_possible(self.possible())
        self.cell_2.set_possible(self.possible())

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:
        upper = int(log10(self.board.maximum_digit)) + 1
        l_1 = LpVariable(f"{self.name}_1", 0, upper, LpContinuous)
        l_2 = LpVariable(f"{self.name}_2", 0, upper, LpContinuous)
        log_1 = lpSum(
            [
                log10(digit) * solver.choices[digit][self.cell_1.row][self.cell_1.column]
                for digit in self.board.digit_range]
        )
        log_2 = lpSum(
            [
                log10(digit) * solver.choices[digit][self.cell_2.row][self.cell_2.column]
                for digit in self.board.digit_range
            ]
        )
        solver.model += l_1 == log_1, f"{self.name}_a_1"
        solver.model += l_2 == log_2, f"{self.name}_a_2"
        name = f"{self.name}_{self.cell_1.row}_{self.cell_1.column}_{self.cell_2.row}_{self.cell_2.column}"
        solver.model += Formulations.abs(solver, l_1, l_2, upper) == log10(self.ratio), name

    def css(self) -> Dict:
        return {
            '.ProductPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black',
                'background': 'transparent'
            }
        }
