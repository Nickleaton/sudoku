"""BetweenLine."""
from typing import List, Dict

from pulp import LpVariable, LpInteger

from src.glyphs.between_line_glyph import BetweenLineGlyph
from src.glyphs.glyph import Glyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule

EXCLUDE_VALUES_ON_LINE = False


class BetweenLine(Line):
    """Represent a line between two filled circles in a puzzle.

    The values in the cells along this line must strictly fall between the
    values in the filled circles at either end of the line.

    Attributes:
        None directly defined; inherits from Line.
    """

    @property
    def rules(self) -> List[Rule]:
        """Define the rules associated with the BetweenLine.

        Returns:
            List[Rule]: A list containing rules related to the BetweenLine.
        """
        return [
            Rule(
                'BetweenLine',
                1,
                "Cells along lines between two filled circles must have values strictly between those in the circles"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Create glyph representations of the BetweenLine for rendering.

        Returns:
            List[Glyph]: A list containing a BetweenLineGlyph for graphical representation.
        """
        return [BetweenLineGlyph('BetweenLine', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Define tags associated with the BetweenLine.

        Returns:
            set[str]: A set of tags that categorize the BetweenLine.
        """
        return super().tags.union({'BetweenLine', 'Comparison'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add puzzle constraints for the BetweenLine to the solver.

        The constraints enforce that the values in cells between the filled circles
        are strictly greater than the starting circle's value and strictly less than
        the ending circle's value.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        big_m = solver.board.maximum_digit + 1

        start_cell = self.cells[0]
        start = solver.values[start_cell.row][start_cell.column]

        end_cell = self.cells[-1]
        end = solver.values[end_cell.row][end_cell.column]

        flag = LpVariable(f"{self.name}_increasing", 0, 1, LpInteger)

        for cell in self.cells[1:-1]:
            value = solver.values[cell.row][cell.column]

            # Ascending constraints
            label = f"{self.name}_after_ascending_{cell.row}_{cell.column}"
            solver.model += start + 1 <= big_m * flag + value, label

            label = f"{self.name}_before_ascending_{cell.row}_{cell.column}"
            solver.model += value + 1 <= big_m * flag + end, label

            # Descending constraints
            label = f"{self.name}_after_descending_{cell.row}_{cell.column}"
            solver.model += start + big_m * (1 - flag) >= value + 1, label

            label = f"{self.name}_before_descending_{cell.row}_{cell.column}"
            solver.model += value + big_m * (1 - flag) >= end + 1, label

            name = f"{self.name}_s_{1}_{cell.row}_{cell.column}"
            solver.model += solver.choices[1][cell.row][cell.column] == 0, name

            name = f"{self.name}_e_{1}_{cell.row}_{cell.column}"
            solver.model += solver.choices[self.board.maximum_digit][cell.row][cell.column] == 0, name

    def css(self) -> Dict:
        """Define the CSS style for rendering the BetweenLine.

        Returns:
            Dict: CSS styling for the BetweenLine, specifying stroke and fill colors.
        """
        return {
            '.BetweenLine': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.BetweenStart': {
                # Style for the start of the line can be added here
            },
            '.BetweenEnd': {
                # Style for the end of the line can be added here
            }
        }
