from typing import List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.items.line import Line
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class MaxArrowLine(Line):
    """A specialized Line that represents a maximum constraint on an arrow.

    The MaxArrowLine enforces a rule where the digit in the bulb (start) of
    the arrow is the maximum of the digits along the arrow.
    """

    @property
    def rules(self) -> List[Rule]:
        """Defines rules specific to MaxArrowLine.

        Returns:
            List[Rule]: A list containing a single Rule object that specifies:
            - The digit in the bulb is the maximum of the digits on the arrow.
        """
        return [
            Rule(
                'MaxArrowLine',
                1,
                "The digit in the bulb is the maximum of the digits on the arrow"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """Generates a graphical representation of the MaxArrowLine.

        Returns:
            List[Glyph]: A list containing an `ArrowLineGlyph` instance with
            cell coordinates for display as a maximum arrow line.
        """
        return [ArrowLineGlyph('MaxArrowLine', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the MaxArrowLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the MaxArrowLine.
        """
        return super().tags.union({'Arrow', 'MaxArrowLine'})

    def css(self) -> Dict:
        """CSS styles for rendering the MaxArrowLine in the user interface.

        Returns:
            Dict: A dictionary defining CSS properties for `.MaxArrowLine` to
            style this line visually as a maximum arrow line.
        """
        return {
            '.MaxArrowLine': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.MaxArrowStart': {
            },
            '.MaxArrowEnd': {
                'fill-opacity': 0
            }
        }

    def add_constraint(self, solver: PulpSolver) -> None:
        """Adds maximum constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints
            for the MaxArrowLine will be added.

        This method uses the maximum formulation to ensure that the bulb
        cell value is equal to the maximum of the arrow's cell values.
        """
        bulb = solver.values[self.cells[0].row][self.cells[0].column]
        values = [solver.values[self.cells[i].row][self.cells[i].column] for i in range(1, len(self.cells))]
        value = Formulations.maximum(solver.model, values, 1, self.board.maximum_digit)
        solver.model += bulb == value, self.name
