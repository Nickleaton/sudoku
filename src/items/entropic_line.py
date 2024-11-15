"""EntropicLine."""
from typing import List, Dict

from pulp import LpAffineExpression, lpSum

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class EntropicLine(Line):
    """Represents a line with entropic constraints for a puzzle.

    Each sequence of three successive cells in the line must contain one digit
    each from the low (1-3), medium (4-6), and high (7-9) categories. This
    class provides rules, glyph representations, constraint enforcement, and
    styling for the entropic line.

    """

    @property
    def rules(self) -> List[Rule]:
        """Define the rules for the entropic line.

        Returns:
            List[Rule]: A list containing the entropic rule, enforcing that
            any three successive cells contain low, medium, and high digits.
        """
        return [
            Rule(
                'EntropicLine',
                1,
                (
                    "Any sequence of 3 successive digits along a golden line must include "
                    "a low (123), a medium (456) and a high (789) digit"
                )
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Create glyph representations of the entropic line for rendering.

        Returns:
            List[Glyph]: A list of PolyLineGlyph objects representing the line.
        """
        return [PolyLineGlyph('EntropicLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Provide tags associated with the entropic line.

        Returns:
            set[str]: A set of tags identifying the entropic line.
        """
        return super().tags.union({'EntropicLine', 'Set'})

    def low_total(self, solver: PulpSolver, n: int) -> LpAffineExpression:
        """Calculate the total for low digits in a specified cell.

        Args:
            solver (PulpSolver): The solver instance.
            n (int): The index of the cell in the line.

        Returns:
            LpAffineExpression: The sum of low digits (1, 2, 3) in the cell.
        """
        return lpSum([solver.choices[digit][self.cells[n].row][self.cells[n].column] for digit in [1, 2, 3]])

    def mid_total(self, solver: PulpSolver, n: int) -> LpAffineExpression:
        """Calculate the total for medium digits in a specified cell.

        Args:
            solver (PulpSolver): The solver instance.
            n (int): The index of the cell in the line.

        Returns:
            LpAffineExpression: The sum of medium digits (4, 5, 6) in the cell.
        """
        return lpSum([solver.choices[digit][self.cells[n].row][self.cells[n].column] for digit in [4, 5, 6]])

    def top_total(self, solver: PulpSolver, n: int) -> LpAffineExpression:
        """Calculate the total for high digits in a specified cell.

        Args:
            solver (PulpSolver): The solver instance.
            n (int): The index of the cell in the line.

        Returns:
            LpAffineExpression: The sum of high digits (7, 8, 9) in the cell.
        """
        return lpSum([solver.choices[digit][self.cells[n].row][self.cells[n].column] for digit in [7, 8, 9]])

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for entropic rules to the solver model.

        Enforces two constraints:
        - No two successive cells along the line contain the same category
          of digit (low, medium, or high).
        - Every group of three cells in the line maintains the same entropic
          distribution, with one cell in each group containing low, medium,
          and high digits respectively.

        Args:
            solver (PulpSolver): The solver to which constraints are added.
        """
        # Prevent consecutive cells from containing the same category.
        for i in range(len(self.cells) - 1):
            pname = f"{self.cells[i].row}_{self.cells[i].column}_{self.cells[i + 1].row}_{self.cells[i + 1].column}"
            solver.model += self.low_total(solver, i) + self.low_total(solver, i + 1) <= 1, f"{self.name}_a_low_{pname}"
            solver.model += self.mid_total(solver, i) + self.mid_total(solver, i + 1) <= 1, f"{self.name}_a_mid_{pname}"
            solver.model += self.top_total(solver, i) + self.top_total(solver, i + 1) <= 1, f"{self.name}_a_top_{pname}"
        # Enforce every 3 cells to follow the same entropic pattern.
        for i in range(len(self.cells) - 3):
            pname = f"{self.cells[i].row}_{self.cells[i].column}_{self.cells[i + 3].row}_{self.cells[i + 3].column}"
            solver.model += self.low_total(solver, i) == self.low_total(solver, i + 3), f"{self.name}_j_low_{pname}"
            solver.model += self.mid_total(solver, i) == self.mid_total(solver, i + 3), f"{self.name}_j_mid_{pname}"
            solver.model += self.top_total(solver, i) == self.top_total(solver, i + 3), f"{self.name}_j_top_{pname}"

    def css(self) -> Dict:
        """Define the CSS style for rendering the entropic line.

        Returns:
            Dict: CSS styling for the line, setting color and stroke properties.
        """
        return {
            '.EntropicLine': {
                'stroke': 'orange',
                'stroke-width': 10,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0
            }
        }

