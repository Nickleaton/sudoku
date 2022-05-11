from typing import List

from src.glyphs.glyph import Glyph, PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Mountain(Line):

    @property
    def rules(self) -> List[Rule]:
        return [
            Rule(
                'Mountain',
                1,
                "Lines symbolise mountains. The closer to the top of the mountain, the higher the value in the cell."
            )
        ]

    @property
    def glyphs(self) -> List[Glyph]:
        return [PolyLineGlyph('Mountain', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        return super().tags.union({'Mountain', 'Adjacent', 'Set'})

    def add_constraint(self, solver: PulpSolver) -> None:
        for i in range(0, len(self.cells) - 1):
            c1 = self.cells[i]
            c2 = self.cells[i + 1]
            name = f"{self.name}_{i}"
            if c1.row < c2.row:
                solver.model += solver.values[c1.row][c1.column] >= solver.values[c2.row][c2.column] + 1, name
            else:
                solver.model += solver.values[c1.row][c1.column] <= solver.values[c2.row][c2.column] - 1, name
