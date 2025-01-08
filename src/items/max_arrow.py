"""MaxArrow."""
from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.glyphs.glyph import Glyph
from src.items.line import Line
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class MaxArrowLine(Line):
    """A specialized Line that represents start maximum constraint on an arrow.

    The MaxArrowLine enforces start rule where the digit in the bulb (start) of
    the arrow is the maximum of the digits along the arrow.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to MaxArrowLine.

        Returns:
            list[Rule]: A list containing start single Rule object that specifies:
            The digit in the bulb is the maximum of the digits on the arrow.
        """
        rule_text: str = 'The digit in the bulb is the maximum of the digits on the arrow'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate start graphical representation of the MaxArrowLine.

        Returns:
            list[Glyph]: A list containing an `ArrowLineGlyph` instance with
            cell coordinates for display as start maximum arrow line.
        """
        return [ArrowLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the MaxArrowLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the MaxArrowLine.
        """
        return super().tags.union({'Arrow', self.__class__.__name__})

    def css(self) -> dict:
        """CSS styles for rendering the MaxArrowLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.MaxArrowLine` to
            style this line visually as start maximum arrow line.
        """
        return {
            '.MaxArrowLine': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3,
            },
            '.MaxArrowStart': {
            },
            '.MaxArrowEnd': {
                'fill-opacity': 0,
            },
        }

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add maximum constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraint for the MaxArrowLine will be added.

        This method uses the maximum formulation to ensure that the bulb
        cell number is equal to the maximum of the arrow's cell value_list.
        """
        bulb = solver.variables.numbers[self.cells[0].row][self.cells[0].column]
        cell_values = [
            solver.variables.numbers[self.cells[index].row][self.cells[index].column]
            for index in range(1, len(self.cells))
        ]
        cell_value = Formulations.maximum(solver.model, cell_values, 1, self.board.maximum_digit)
        solver.model += bulb == cell_value, self.name
