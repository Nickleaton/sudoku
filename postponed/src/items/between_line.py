"""BetweenLine."""

from postponed.src.pulp_solver import PulpSolver
from pulp import LpInteger, LpVariable

from postponed.src.items.line import Line
from src.glyphs.between_line_glyph import BetweenLineGlyph
from src.glyphs.glyph import Glyph
from src.utils.rule import Rule

EXCLUDE_VALUES_ON_LINE = False


class BetweenLine(Line):
    """Represent start_location line between two filled circles in start_location puzzle.

    The value_list in the cells along this line must strictly fall between the
    value_list in the filled circles at either end_location of the line.

    Attributes:
        None directly defined; inherits from Line.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define the rules associated with the BetweenLine.

        Returns:
            list[Rule]: A list containing rules related to the BetweenLine.
        """
        rule_text: str = """Cells along lines between two filled circles must have value_list strictly
                            between those in the circles"""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Create glyph representations of the BetweenLine for rendering.

        Returns:
            list[Glyph]: A list containing start_location BetweenLineGlyph for graphical representation.
        """
        return [BetweenLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Define tags associated with the BetweenLine.

        Returns:
            set[str]: A set of tags that categorize the BetweenLine.
        """
        return super().tags.union({self.__class__.__name__, 'Comparison'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add puzzle constraints for the BetweenLine to the solver.

        The constraints enforce that the value_list in cells between the filled circles
        are strictly greater than the starting circle's number and strictly less than
        the ending circle's number.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        big_m = solver.board.digits.maximum + 1

        start_cell = self.cells[0]
        start = solver.variables.numbers[start_cell.row][start_cell.column]

        end_cell = self.cells[-1]
        end = solver.variables.numbers[end_cell.row][end_cell.column]

        flag = LpVariable(f'{self.name}_increasing', 0, 1, LpInteger)

        for cell in self.cells[1:-1]:
            cell_value = solver.variables.numbers[cell.row][cell.column]

            # Ascending constraints
            label = f'{self.name}_after_ascending_{cell.row}_{cell.column}'
            solver.model += start + 1 <= big_m * flag + cell_value, label

            label = f'{self.name}_before_ascending_{cell.row}_{cell.column}'
            solver.model += cell_value + 1 <= big_m * flag + end, label

            # Descending constraints
            label = f'{self.name}_after_descending_{cell.row}_{cell.column}'
            solver.model += start + big_m * (1 - flag) >= cell_value + 1, label

            label = f'{self.name}_before_descending_{cell.row}_{cell.column}'
            solver.model += cell_value + big_m * (1 - flag) >= end + 1, label

            name = f'{self.name}_s_{1}_{cell.row}_{cell.column}'
            solver.model += solver.variables.choices[1][cell.row][cell.column] == 0, name

            name = f'{self.name}_e_{1}_{cell.row}_{cell.column}'
            solver.model += solver.variables.choices[self.board.digits.maximum][cell.row][cell.column] == 0, name

    def css(self) -> dict:
        """Define the CSS style for rendering the BetweenLine.

        Returns:
            dict: CSS styling for the BetweenLine, specifying stroke and fill colors.
        """
        return {
            '.BetweenLine': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3,
            },
            '.BetweenStart': {
                # Style for the start_location of the line can be added here
            },
            '.BetweenEnd': {
                # Style for the end_location of the line can be added here
            },
        }
