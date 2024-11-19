"""SequenceLine."""
from pulp import LpVariable, LpInteger

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SequenceLine(Line):
    """A specialized Line that represents an arithmetic sequence constraint.

    The SequenceLine enforces a rule where digits along a grey line form an
    arithmetic sequence, going in increasing order with a consistent difference
    between consecutive cells.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to SequenceLine.

        Returns:
            list[Rule]: A list containing a single Rule object that specifies:
            - Digits along grey lines follow an arithmetic sequence.
        """
        return [
            Rule(
                'SequenceLine',
                1,
                (
                    "Digits along grey lines follow arithmetic sequences. "
                    "They increase from one end to the other with a constant difference."
                )
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Generate a graphical representation of the SequenceLine.

        Returns:
            list[Glyph]: A list containing a `PolyLineGlyph` instance with
            cell coordinates for display as a sequence line.
        """
        return [PolyLineGlyph('SequenceLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the SequenceLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the SequenceLine.
        """
        return super().tags.union({'SequenceLine', 'Difference'})

    @staticmethod
    def max_difference(length: int) -> int:
        """Determine the maximum possible difference for an arithmetic sequence of a given length.

        Args:
            length (int): The length of the sequence.

        Returns:
            int: The maximum allowable difference between consecutive values in the sequence.
        """
        if length == 1:
            return 9
        if length == 2:
            return 8
        if length == 3:
            return 3
        if length == 4:
            return 2
        if length == 5:
            return 2
        return 1

    def possible_digits(self) -> list[set[int]]:
        """Determine possible digits for each cell along the sequence.

        Returns:
            list[set[int]]: A list of sets containing possible digits for each
            cell, based on the maximum digit and length of the sequence.
        """
        length = len(self.cells)
        big_m = self.board.maximum_digit

        possible = []
        for i in range(1, length + 1):
            a = set(range(i, i + big_m - length + 1))
            # pylint: disable=loop-invariant-statement
            d = {big_m - x + 1 for x in range(i, i + big_m - length + 1)}
            possible.append(a.union(d))
        return possible

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add arithmetic sequence constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints
            for the SequenceLine will be added.

        Constraints include uniqueness, sequence difference, and restricting possible
        digits to speed solving.
        """
        # Ensure the cells in the sequence have unique values
        self.add_unique_constraint(solver, optional=True)

        # Create a variable for the difference between consecutive cells
        max_diff = SequenceLine.max_difference(len(self.cells))
        difference = LpVariable(self.name, -max_diff, max_diff, LpInteger)

        # Set the constraint for each consecutive pair of cells
        for i in range(len(self.cells) - 1):
            value1 = solver.values[self.cells[i].row][self.cells[i].column]
            value2 = solver.values[self.cells[i + 1].row][self.cells[i + 1].column]
            solver.model += value1 - value2 == difference, f"{self.name}_{i}"

        # Restrict possible digits for each cell along the line
        for i, possible in enumerate(self.possible_digits()):
            for d in self.board.digit_range:
                if d not in possible:
                    cell = self.cells[i]
                    name = f"{self.name}_impossible_{i}_{d}"
                    solver.model += solver.choices[d][cell.row][cell.column] == 0, name

    def css(self) -> dict:
        """CSS styles for rendering the SequenceLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.RenbanLine` to style
            this line as a sequence line.
        """
        return {
            ".SequenceLine": {
                "stroke": "grey",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
