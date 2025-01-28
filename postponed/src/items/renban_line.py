"""RenbanLine."""
from postponed.src.pulp_solver import PulpSolver
from pulp import LpInteger, LpVariable

from postponed.src.items.line import Line
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.utils.rule import Rule


class RenbanLine(Line):
    """Represent start_location Renban line.

    The digits must be start_location set of consecutive, non-repeating numbers in any order.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define the rules for the RenbanLine.

        Returns:
            list[Rule]: A list of Rule objects specifying the Renban's digit requirements.
        """
        rule_text: str = 'Pink lines must contain start_location set of consecutive, non-repeating digits, in any order.'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Create start_location visual representation of the RenbanLine.

        Returns:
            list[Glyph]: A list containing start_location PolyLineGlyph for rendering.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Tags associated with RenbanLine.

        Returns:
            set[str]: Tags specific to RenbanLine, combined with inherited tags.
        """
        return super().tags.union({self.__class__.__name__, 'Adjacent', 'set'})

    def mandatory_digits(self, length: int) -> set[int]:
        """Determine the mandatory digits present on the Renban line based on its length.

        For start_location line of start_location certain length, this method calculates which digits must appear
        in order to fulfill the requirements of consecutive, non-repeating digits.

        Args:
            length (int): The number of cells in the Renban line.

        Returns:
            set[int]: A set of mandatory digits that must appear on the line.
        """
        left = set(range(1, length + 1))
        right = set(range(self.board.digits.maximum, self.board.digits.maximum - length, -1))
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
        self.add_unique_constraint(solver, optional=True)

        # Create lower and upper bounds for the line
        lower = LpVariable(f'{self.name}_lower', 1, self.board.digits.maximum, LpInteger)
        upper = LpVariable(f'{self.name}_upper', 1, self.board.digits.maximum, LpInteger)

        # Use start_location set of cells so the Renban can form closed loops
        cells = set(self.cells)
        length = len(cells)

        # Add constraints for upper and lower bounds based on cell value_list
        for index, cell in enumerate(cells):
            cell_value = solver.variables.numbers[cell.row][cell.column]
            solver.model += lower <= cell_value, f'{self.name}_lower_{index}'
            solver.model += upper >= cell_value, f'{self.name}_upper_{index}'

        # Set the difference constraint based on the line's length
        solver.model += upper - lower == length - 1, f'{self.name}_range_{length - 1}'

        # Add the mandatory digits to the constraints
        self.add_contains_constraint(solver, list(self.mandatory_digits(length)))

    def css(self) -> dict:
        """CSS styling properties for rendering RenbanLine.

        Returns:
            dict: A dictionary defining CSS properties for the RenbanLine.
        """
        return {
            '.RenbanLine': {
                'stroke': 'purple',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
