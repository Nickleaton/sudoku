import re
from typing import List, Sequence, Set, Optional

from pulp import lpSum

from src.items.board import Board
from src.items.box import Box
from src.items.cell import Cell
from src.items.column import Column
from src.items.difference_line import DifferenceLine
from src.items.greater_than_equal_difference_pair import GreaterThanEqualDifferencePair
from src.items.row import Row
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class GreaterThanEqualDifferenceLine(DifferenceLine):

    def __init__(self, board: Board, cells: Sequence[Cell], difference: int = 0):
        super().__init__(board, cells, difference)
        for i in range(1, len(cells)):
            self.add(GreaterThanEqualDifferencePair(self.board, cells[i - 1], cells[i], self.difference))

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                self.__class__.__name__,
                1,
                f"Any two cells directly connected by a line must have a difference of at least {self.difference}"
            )
        ]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Difference', 'Comparison'})

    @staticmethod
    def get_regions(cell: Cell) -> Set:
        regions = {region for region in cell.top.regions()}
        result: Set = set({})
        for r in regions:
            if r.__class__ in [Box, Column, Row]:
                if cell in r:
                    result.add(r)
        return result

    def add_constraint(self, solver: PulpSolver) -> None:

        # # add a constraint for values that are impossible on a line. e.g. 5 on a GermanWhispers
        # for cell in self.cells:
        #     for digit in self.board.digit_range:
        #         if abs(1 - digit) < self.difference and abs(self.board.maximum_digit - digit) < self.difference:
        #             name = f"{self.name}_{cell.name}_{digit}_not_allowed_1"
        #             solver.model += solver.choices[digit][cell.row][cell.column] == 0, name

        # make sure that the difference is at least the difference
        for i in range(0, len(self.cells) - 1):
            for digit in self.board.digit_range:
                name = f"{self.name}_{i}_{digit}"
                total = lpSum(
                    [
                        solver.choices[d][self.cells[i + 1].row][self.cells[i + 1].column]
                        for d in self.board.digit_range if abs(d - digit) >= self.difference
                    ]
                )
                first = solver.choices[digit][self.cells[i].row][self.cells[i].column]
                solver.model += first <= total, name

        for i in range(1, len(self.cells) - 1):
            c0 = self.cells[i - 1]
            c1 = self.cells[i - 0]
            c2 = self.cells[i + 1]
            r0 = GreaterThanEqualDifferenceLine.get_regions(c0)
            r1 = GreaterThanEqualDifferenceLine.get_regions(c1)
            r2 = GreaterThanEqualDifferenceLine.get_regions(c2)
            intersection = r0.intersection(r1).intersection(r2)

            if len(intersection) != 0:
                # print(c0, c1, c2)
                # for r in intersection:
                #     print(r)
                for digit in [4, 6]:
                    name = f"{self.name}_{self.cells[i].name}_{digit}_not_allowed"
                    solver.model += solver.choices[digit][self.cells[i].row][self.cells[i].column] == 0, name
