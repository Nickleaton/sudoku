import re
from typing import List, Dict

from pulp import lpSum

from src.glyphs.glyph import Glyph, ArrowLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Arrow(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Arrow',
                1,
                "Digits along an arrow must sum to the digit in its circle. Digits may repeat along an arrow"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Arrow', 'Sum'})

    def css(self) -> Dict:
        return {
            '.Arrow': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.ArrowStart': {
            },
            '.ArrowEnd': {
                'fill-opacity': 0
            }
        }

    def add_constraint(self, solver: PulpSolver, include: re.Pattern, exclude: re.Pattern) -> None:

        def triangular(n: int) -> int:
            return n * (n + 1) // 2

        total = lpSum([solver.values[self.cells[i].row][self.cells[i].column] for i in range(1, len(self))])
        solver.model += total == solver.values[self.cells[0].row][self.cells[0].column], self.name

        if len(self.cells) == 2:
            for digit in self.board.digit_range:
                d1 = solver.choices[digit][self.cells[0].row][self.cells[0].column]
                d2 = solver.choices[digit][self.cells[1].row][self.cells[1].column]
                solver.model += d1 == d2, f"{self.name}_one_cell_{digit}"
            return

        # needed to get times down.
        # simple restriction using boxes

        # get the cells not on the head and find which box they are in
        regions = {}
        for i in range(1, len(self.cells)):
            box = self.board.box_index(self.cells[i].row, self.cells[i].column)
            if box not in regions:
                regions[box] = []
            regions[box].append(self.cells[i])

        # If we have n cells in a given region, the mimimum total is the triangular number for n
        # Add them all up
        total = 0
        for v in regions.values():
            total += triangular(len(v))

        solver.model += solver.values[self.cells[0].row][self.cells[0].column] >= total, f"{self.name}_head"
        for digit in self.board.digit_range:
            if digit >= total:
                continue
            choice = solver.choices[digit][self.cells[0].row][self.cells[0].column]
            solver.model += choice == 0, f"{self.name}_{i}_{digit}_head"

        for i in range(1, len(self.cells)):
            # value = solver.values[self.cells[i].row][self.cells[i].column]
            for digit in self.board.digit_range:
                if digit <= self.board.maximum_digit - total + 1:
                    continue
                choice = solver.choices[digit][self.cells[i].row][self.cells[i].column]
                solver.model += choice == 0, f"{self.name}_{i}_{digit}_tail"
