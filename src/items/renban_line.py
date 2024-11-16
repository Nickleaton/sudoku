"""RenbanLine."""
from typing import List, Set, Dict

from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class RenbanLine(Line):
    """Represent a Renban line.

    The digits must be a set of consecutive, non-repeating numbers in any order.
    """

    @property
    def rules(self) -> List[Rule]:
        """Define the rules for the RenbanLine.

        Returns:
            List[Rule]: A list of Rule objects specifying the Renban's digit requirements.
        """
        return [
            Rule(
                'RenbanLine',
                1,
                "Pink lines must contain a set of consecutive, non-repeating digits, in any order."
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Create a visual representation of the RenbanLine.

        Returns:
            List[Glyph]: A list containing a PolyLineGlyph for rendering.
        """
        return [PolyLineGlyph('RenbanLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Tags associated with RenbanLine.

        Returns:
            set[str]: Tags specific to RenbanLine, combined with inherited tags.
        """
        return super().tags.union({'RenbanLine', 'Adjacent', 'Set'})

    def mandatory_digits(self, length: int) -> Set[int]:
        """Determine the mandatory digits present on the Renban line based on its length.

        For a line of a certain length, this method calculates which digits must appear
        in order to fulfill the requirements of consecutive, non-repeating digits.

        Args:
            length (int): The number of cells in the Renban line.

        Returns:
            Set[int]: A set of mandatory digits that must appear on the line.
        """
        left = set(range(1, length + 1))
        right = set(range(self.board.maximum_digit, self.board.maximum_digit - length, -1))
        return left & right

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the Pulp solver to enforce the Renban line rules.

        This includes uniqueness of digits, bounds for the minimum and maximum digits,
        and the total range of digits based on the line's length.

        Args:
            solver (PulpSolver): The Pulp solver instance to which constraints will be added.
        """
        # Ensure uniqueness of digits on the line
        self.add_unique_constraint(solver, True)

        # Create lower and upper bounds for the line
        lower = LpVariable(f"{self.name}_lower", 1, self.board.maximum_digit, LpInteger)
        upper = LpVariable(f"{self.name}_upper", 1, self.board.maximum_digit, LpInteger)

        # Use a set of cells so the Renban can form closed loops
        cells = set(self.cells)
        length = len(cells)

        # Add constraints for upper and lower bounds based on cell values
        for i, cell in enumerate(cells):
            value = solver.values[cell.row][cell.column]
            solver.model += lower <= value, f"{self.name}_lower_{i}"
            solver.model += upper >= value, f"{self.name}_upper_{i}"

        # Set the difference constraint based on the line's length
        solver.model += upper - lower == length - 1, f"{self.name}_range_{length - 1}"

        # Add the mandatory digits to the constraints
        self.add_contains_constraint(solver, list(self.mandatory_digits(length)))

    def css(self) -> Dict:
        """CSS styling properties for rendering RenbanLine.

        Returns:
            Dict: A dictionary defining CSS properties for the RenbanLine.
        """
        return {
            ".RenbanLine": {
                "stroke": "purple",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
