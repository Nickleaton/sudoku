from typing import List

from pulp import lpSum

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class EqualSum(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'EqualSum',
                1,
                "For each line, digits on the line have an equal sum N within each 3x3 box it passes through. "
                "If a line passes through the same box more than once, "
                "each individual segment of such a line within that box sums to N separately"
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('EqualSum', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'EqualSum', 'Sum'})

    def add_constraint(self, solver: PulpSolver) -> None:
        # Build areas
        areas = []
        current = 0
        for cell in self.cells:
            box = self.board.box_index(cell.row, cell.column)
            if box != current:
                areas.append([])
                current = box
            areas[-1].append(cell)

        # Cannot exceed the digit sum.
        # total = LpVariable(f"{self.name}_total", cat='Integer', lowBound=1, upBound=self.board.digit_sum)
        # for i, region in enumerate(areas):
        #     cell_sum = lpSum([solver.values[cell.row][cell.column] for cell in region])
        #     solver.model += total == cell_sum, f"{self.name}_{i}"

        # create a sum for each area
        sums = []
        for region in areas:
            sums.append(lpSum([solver.values[cell.row][cell.column] for cell in region]))

        # set total[i] = total[i+1]
        for i in range(0, len(areas)):
            j = 0 if i == len(areas) - 1 else i + 1
            solver.model += sums[i] == sums[j], f"{self.name}_{i}"
