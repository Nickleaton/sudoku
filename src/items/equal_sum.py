import sys
from typing import List, Dict

from pulp import lpSum

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell
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

    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('EqualSum', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'EqualSum', 'Sum'})

    def add_constraint(self, solver: PulpSolver) -> None:
        # Build areas
        areas: List[List[Cell]] = []
        current = 0
        for cell in self.cells:
            box = self.board.box_index(cell.row, cell.column)
            if box != current:
                areas.append([])
                current = box
            areas[-1].append(cell)

        # create a sum for each area
        sums = []
        for region in areas:
            sums.append(lpSum([solver.values[cell.row][cell.column] for cell in region]))

        # set total[i] = total[i+1]
        for i in range(0, len(areas)):
            j = 0 if i == len(areas) - 1 else i + 1
            solver.model += sums[i] == sums[j], f"{self.name}_{i}"

        minimum = 0
        maximum = sys.maxsize
        for region in areas:
            minimum = max(minimum, sum([i + 1 for i in range(0, len(region))]))
            maximum = min(maximum, sum([(self.board.maximum_digit - i) for i in range(0, len(region))]))

        for i in range(0, len(areas)):
            solver.model += sums[i] >= minimum, f"{self.name}_minimum_{i}"
            solver.model += sums[i] <= maximum, f"{self.name}_maximum_{i}"

    def css(self) -> Dict:
        return {
            '.EqualSum': {
                'stroke': 'lightskyblue',
                'stroke-width': 10,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }
