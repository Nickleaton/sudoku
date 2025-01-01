"""SimpleThermometerLine."""

from src.glyphs.glyph import Glyph
from src.glyphs.thermometer_glyph import ThermometerGlyph
from src.items.cell import Cell
from src.items.thermometer_line import ThermometerLine
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class SimpleThermometerLine(ThermometerLine):
    """Simple thermometer line.

    Cells along the line must strictly increase from the bulb end.
    """

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the Simple Thermometer line.

        Returns:
            list[Rule]: A list of rules specific to the Simple Thermometer line.
        """
        rule_text: str = 'Cells along start line with start bulb strictly increase from the bulb end'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate glyph representations for the Simple Thermometer line.

        Returns:
            list[Glyph]: A list of glyphs representing the Simple Thermometer line.
        """
        return [ThermometerGlyph(self.__class__.__name__, [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Simple Thermometer line.

        Returns:
            set[str]: A set of tags specific to the Simple Thermometer line.
        """
        return super().tags.union({self.__class__.__name__})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to the solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        self.add_rank_constraints(solver)
        self.add_bounds_constraints(solver)

    def add_rank_constraints(self, solver: PulpSolver) -> None:
        """Add constraints that enforce the ranking order between consecutive cells.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        for cell1, cell2 in zip(self.cells[:-1], self.cells[1:]):
            cell1_value = solver.cell_values[cell1.row][cell1.column]
            cell2_value = solver.cell_values[cell2.row][cell2.column]
            # C1 < C2 constraint
            name: str = f'{self.name}_rank_{cell1.row}_{cell1.column}_{cell2.row}_{cell2.column}'
            solver.model += cell1_value + 1 <= cell2_value, name

    def add_bounds_constraints(self, solver: PulpSolver) -> None:
        """Add bounds constraints for each cell in the sequence.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        for index, cell in enumerate(self.cells):
            lower: int = index + 1
            upper: int = self.board.maximum_digit - len(self) + index + 1
            self.add_possible_digit_restrictions(solver, cell, lower, upper)

    def add_possible_digit_restrictions(self, solver: PulpSolver, cell: Cell, lower: int, upper: int) -> None:
        """Add restrictions for digits that are not possible for a given cell.

        Args:
            solver (PulpSolver): The solver instance to which the restrictions are added.
            cell (Cell): The cell to which the restrictions are applied.
            lower (int): The lower bound for the possible cell_values.
            upper (int): The upper bound for the possible cell_values.
        """
        possible_digits = set(range(lower, upper + 1))
        for digit in self.board.digit_range:
            if digit not in possible_digits:
                solver.model += solver.choices[digit][cell.row][cell.column] == 0, f'{self.name}_{cell.name}_{digit}'
