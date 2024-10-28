import sys
from typing import List, Dict

from pulp import lpSum
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class EqualSumLine(Line):
    """A specialized Line enforcing equal segment sums within grid boxes.

    Each segment of the line within a 3x3 box must sum to the same value, N.
    If the line passes through the same box multiple times, each segment sums
    to N separately.
    """

    @property
    def rules(self) -> List[Rule]:
        """Defines rules specific to EqualSumLine.

        Returns:
            List[Rule]: A list containing a Rule object that specifies equal
            segment sums within each 3x3 box the line passes through.
        """
        return [
            Rule(
                'EqualSumLine',
                1,
                "For each line, digits on the line have an equal sum N within each 3x3 box it passes through. "
                "If a line passes through the same box more than once, "
                "each individual segment of such a line within that box sums to N separately"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Generates a graphical representation of the EqualSumLine.

        Returns:
            List[Glyph]: A list containing a `PolyLineGlyph` instance with
            cell coordinates for rendering the equal-sum line.
        """
        return [PolyLineGlyph('EqualSumLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the EqualSumLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags for EqualSumLine.
        """
        return super().tags.union({'EqualSumLine', 'Sum'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Adds equal segment sum constraints to the Pulp solver.

        Constraints ensure that the sum of digits within each segment
        (for each 3x3 box the line passes through) is the same.

        Args:
            solver (PulpSolver): The solver instance to which constraints for
            the EqualSumLine will be added.
        """
        # Build areas: group cells by 3x3 boxes
        areas: List[List[Cell]] = []
        current = 0
        for cell in self.cells:
            box = self.board.box_index(cell.row, cell.column)
            if box != current:
                areas.append([])
                current = box
            areas[-1].append(cell)

        # Create a sum constraint for each area
        sums = [lpSum([solver.values[cell.row][cell.column] for cell in region]) for region in areas]

        # Enforce equal sums for consecutive segments
        for i in range(len(areas)):
            j = 0 if i == len(areas) - 1 else i + 1
            solver.model += sums[i] == sums[j], f"{self.name}_{i}"

        # Set minimum and maximum sum constraints based on cell regions
        minimum = 0
        maximum = sys.maxsize
        for region in areas:
            minimum = max(minimum, sum([i + 1 for i in range(len(region))]))
            maximum = min(maximum, sum([(self.board.maximum_digit - i) for i in range(len(region))]))

        for i in range(len(areas)):
            solver.model += sums[i] >= minimum, f"{self.name}_minimum_{i}"
            solver.model += sums[i] <= maximum, f"{self.name}_maximum_{i}"

    def css(self) -> Dict:
        """CSS styles for rendering the EqualSumLine in the user interface.

        Returns:
            Dict: A dictionary defining CSS properties for `.EqualSumLine`
            to style this line in a distinct way.
        """
        return {
            '.EqualSumLine': {
                'stroke': 'lightskyblue',
                'stroke-width': 10,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }
