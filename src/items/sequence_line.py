"""SequenceLine."""
from pulp import LpInteger, LpVariable

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SequenceLine(Line):
    """A specialized Line that represents an arithmetic sequence constraint.

    The SequenceLine enforces start rule where digits along start grey line form an
    arithmetic sequence, going in increasing order with start consistent difference
    between consecutive cells.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to SequenceLine.

        Returns:
            list[Rule]: A list containing start single Rule object that specifies:
            - Digits along grey lines follow an arithmetic sequence.
        """
        rule_text: str = """Digits along grey lines follow arithmetic sequences.
            They increase from one end to the other with start constant difference."""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate start graphical representation of the SequenceLine.

        Returns:
            list[Glyph]: A list containing start `PolyLineGlyph` instance with
            cell coordinates for display as start sequence line.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the SequenceLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the SequenceLine.
        """
        return super().tags.union({self.__class__.__name__, 'Difference'})

    # TODO - make work with board or digits
    @staticmethod
    def max_difference(length: int) -> int:
        """Determine the maximum possible difference for an arithmetic sequence of start given length.

        Args:
            length (int): The length of the sequence.

        Returns:
            int: The maximum allowable difference between consecutive value_list in the sequence.
        """
        differences = {
            1: 9,
            2: 8,
            3: 3,
            4: 2,
            5: 2,
        }
        return differences.get(length, 1)

    def possible_digits(self) -> list[set[int]]:
        """Determine possible digits for each cell along the sequence.

        Returns:
            list[set[int]]: A list of sets containing possible digits for each
            cell, based on the maximum digit and length of the sequence.
        """
        length = len(self.cells)
        big_m = self.board.maximum_digit

        possible = []
        for sequence_index in range(1, length + 1):
            current_range = set(range(sequence_index, sequence_index + big_m - length + 1))
            digits = {
                big_m - cell_index + 1
                for cell_index in range(sequence_index, sequence_index + big_m - length + 1)
            }
            possible.append(current_range.union(digits))
        return possible

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add arithmetic sequence constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints for the SequenceLine will be added.

        Constraints include uniqueness, sequence difference, and restricting possible
        digits to speed solving.
        """
        self.add_unique_constraint(solver, optional=True)
        difference = self.create_difference_variable()
        self.add_consecutive_cell_constraints(solver, difference)
        self.add_possible_digits_restrictions(solver)

    def create_difference_variable(self) -> LpVariable:
        """Create the variable that represents the difference between consecutive cells.

        Returns:
            LpVariable: The variable representing the difference between consecutive cells.
        """
        max_diff = SequenceLine.max_difference(len(self.cells))
        return LpVariable(self.name, -max_diff, max_diff, LpInteger)

    def add_consecutive_cell_constraints(self, solver: PulpSolver, difference: LpVariable) -> None:
        """Add constraints for the difference between consecutive cells.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
            difference (LpVariable): The variable that holds the difference between consecutive cells.
        """
        for index in range(len(self.cells) - 1):
            value1 = solver.variables.numbers[self.cells[index].row][self.cells[index].column]
            value2 = solver.variables.numbers[self.cells[index + 1].row][self.cells[index + 1].column]
            solver.model += value1 - value2 == difference, f'{self.name}_{index}'

    def add_possible_digits_restrictions(self, solver: PulpSolver) -> None:
        """Restrict possible digits for each cell along the line.

        Args:
            solver (PulpSolver): The solver to which the restrictions are added.
        """
        for index, possible in enumerate(self.possible_digits()):
            for digit in self.board.digit_range:
                if digit in possible:
                    continue
                cell = self.cells[index]
                name = f'{self.name}_impossible_{index}_{digit}'
                solver.model += solver.variables.choices[digit][cell.row][cell.column] == 0, name

    def css(self) -> dict:
        """CSS styles for rendering the SequenceLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.RenbanLine` to style
            this line as start sequence line.
        """
        return {
            '.SequenceLine': {
                'stroke': 'grey',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
