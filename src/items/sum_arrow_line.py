from typing import List, Dict

from pulp import lpSum

from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SumArrowLine(Line):
    """Represents an arrow line where digits along the line must sum to the digit at the starting (circle) cell.

    Digits on the arrow are allowed to repeat, and the total sum of digits
    along the arrow equals the value in the initial cell.
    """

    @property
    def rules(self) -> List[Rule]:
        """Define the rules for the SumArrowLine.

        Returns:
            List[Rule]: A list of Rule objects specifying the arrow's summing requirement.
        """
        return [
            Rule(
                'SumArrowLine',
                1,
                "Digits along an arrow must sum to the digit in its circle. Digits may repeat along an arrow."
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Create a visual representation of the SumArrowLine.

        Returns:
            List[Glyph]: A list containing an `ArrowLineGlyph` for rendering.
        """
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags associated with SumArrowLine.

        Returns:
            set[str]: Tags specific to SumArrowLine, combined with inherited tags.
        """
        return super().tags.union({'Arrow', 'Sum'})

    def css(self) -> Dict:
        """CSS styling properties for rendering SumArrowLine.

        Returns:
            Dict: A dictionary defining CSS properties for `.SumArrowLine` and its start and end points.
        """
        return {
            '.SumArrowLine': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.SumArrowLineStart': {
            },
            '.SumArrowLineEnd': {
                'fill-opacity': 0
            }
        }

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the Pulp solver to enforce the sum rule along the arrow.

        The cells along the arrow must sum to the value in the starting cell. Additional constraints
        are added to optimize the solution by limiting possible values in specific regions.

        Args:
            solver (PulpSolver): The Pulp solver instance to which constraints will be added.
        """

        # TODO: Move this to utils
        def triangular(n: int) -> int:
            """Calculate the triangular number for `n`, representing the sum of first `n` integers.

            Args:
                n (int): The number of terms in the sum.

            Returns:
                int: The sum of the first `n` integers.
            """
            return n * (n + 1) // 2

        # Sum constraint: the sum of arrow cells must equal the starting cell value
        total = lpSum([solver.values[self.cells[i].row][self.cells[i].column] for i in range(1, len(self))])
        solver.model += total == solver.values[self.cells[0].row][self.cells[0].column], self.name

        # Special case: if there are only two cells, ensure they match
        if len(self.cells) == 2:
            for digit in self.board.digit_range:
                d1 = solver.choices[digit][self.cells[0].row][self.cells[0].column]
                d2 = solver.choices[digit][self.cells[1].row][self.cells[1].column]
                solver.model += d1 == d2, f"{self.name}_one_cell_{digit}"
            return

        # Optimize by constraining cells based on box regions
        regions: Dict[int, List[Cell]] = {}
        for i in range(1, len(self.cells)):
            box = self.board.box_index(self.cells[i].row, self.cells[i].column)
            if box not in regions:
                regions[box] = []
            regions[box].append(self.cells[i])

        # Set minimum sum constraints based on the smallest possible sum per box region
        total = sum(triangular(len(v)) for v in regions.values())
        solver.model += solver.values[self.cells[0].row][self.cells[0].column] >= total, f"{self.name}_head"

        # Further restrictions based on digit values
        for digit in self.board.digit_range:
            if digit >= total:
                continue
            choice = solver.choices[digit][self.cells[0].row][self.cells[0].column]
            solver.model += choice == 0, f"{self.name}_{digit}_head"

        # Restrict possible values in tail cells
        for i in range(1, len(self.cells)):
            for digit in self.board.digit_range:
                if digit <= self.board.maximum_digit - total + 1:
                    continue
                choice = solver.choices[digit][self.cells[i].row][self.cells[i].column]
                solver.model += choice == 0, f"{self.name}_{i}_{digit}_tail"
