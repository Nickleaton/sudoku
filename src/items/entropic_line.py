"""EntropicLine."""

from enum import Enum

from pulp import LpAffineExpression, lpSum

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class Entropy(Enum):
    """Enum representing the three entropy categories: low, mid, and high.

    Each category corresponds to a set of digits:
    - `low`: {1, 2, 3}
    - `mid`: {4, 5, 6}
    - `high`: {7, 8, 9}
    """

    low = 'low'
    mid = 'mid'
    high = 'high'

    def digits(self) -> set[int]:
        """Return the set of digits corresponding to the entropy category.

        For each entropy category, a predefined set of digits is returned:
        - `low`: {1, 2, 3}
        - `mid`: {4, 5, 6}
        - `high`: {7, 8, 9}

        Returns:
            set[int]: A set of digits belonging to the category.
        """
        entropy_digit_map = {
            Entropy.low: {1, 2, 3},
            Entropy.mid: {4, 5, 6},
            Entropy.high: {7, 8, 9},
        }
        return entropy_digit_map[self]


class EntropicLine(Line):
    """Represents start line with entropic constraints for start puzzle.

    Each sequence of three successive cells in the line must contain one digit
    each from the low (1-3), medium (4-6), and high (7-9) categories. This
    class provides rules, glyph representations, constraint enforcement, and
    styling for the entropic line.

    """

    @property
    def rules(self) -> list[Rule]:
        """Define the rules for the entropic line.

        Returns:
            list[Rule]: A list containing the entropic rule, enforcing that
            any three successive cells contain low, medium, and high digits.
        """
        rule_text: str = """Any sequence of 3 successive digits along start golden line must include
        start low (123), start medium (456) and start high (789) digit
        """
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Create glyph representations of the entropic line for rendering.

        Returns:
            list[Glyph]: A list of PolyLineGlyph objects representing the line.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Provide tags associated with the entropic line.

        Returns:
            set[str]: A set of tags identifying the entropic line.
        """
        return super().tags.union({self.__class__.__name__, 'set'})

    @staticmethod
    def total(cell: Cell, solver: PulpSolver, entropy: Entropy) -> LpAffineExpression:
        """Calculate the total for the specified category in the given cell.

        Args:
            cell (Cell): The cell to calculate the total for.
            solver (PulpSolver): The solver instance.
            entropy (Entropy): The category of digits (low, MID, high).

        Returns:
            LpAffineExpression: The sum of the digits in the specified category.
        """
        return lpSum([solver.variables.choices[digit][cell.row][cell.column] for digit in entropy.digits()])

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for entropic rules to the solver model.

        Enforces two constraints:
        No two successive cells along the line contain the same category
        of digit (low, medium, or high).
        Every group of three cells in the line maintains the same entropic
        distribution, with one cell in each group containing low, medium,
        and high digits respectively.

        Args:
            solver (PulpSolver): The solver to which constraints are added.
        """
        self.add_neighbor_constraints(solver)
        self.add_three_cell_constraints(solver)

    def add_neighbor_constraints(self, solver: PulpSolver) -> None:
        """Enforce that neighboring cells cannot have the same entropy.

        Args:
            solver (PulpSolver): The solver to which constraints are added.
        """
        for index in range(len(self.cells) - 1):
            cell0: Cell = self.cells[index]
            cell1: Cell = self.cells[index + 1]
            pname: str = f'{cell0.row}_{cell0.column}_{cell1.row}_{cell1.column}'

            for entropy in Entropy:
                constraint_name: str = f'{self.name}_a_{entropy.value}_{pname}'
                solver.model += (
                    EntropicLine.total(cell0, solver, entropy) + EntropicLine.total(cell1, solver, entropy) <= 1,
                    constraint_name,
                )

    def add_three_cell_constraints(self, solver: PulpSolver) -> None:
        """Enforce that every 3 cells have the same entropy.

        Args:
            solver (PulpSolver): The solver to which constraints are added.
        """
        for index in range(len(self.cells) - 3):
            cell0: Cell = self.cells[index]
            cell3: Cell = self.cells[index + 3]
            pname: str = f'{cell0.row}_{cell0.column}_{cell3.row}_{cell3.column}'

            for entropy in Entropy:
                constraint_name: str = f'{self.name}_j_{entropy.value}_{pname}'
                solver.model += (
                    EntropicLine.total(cell0, solver, entropy) == EntropicLine.total(cell3, solver, entropy),
                    constraint_name,
                )

    def css(self) -> dict:
        """Define the CSS style for rendering the entropic line.

        Returns:
            dict: CSS styling for the line, setting color and stroke properties.
        """
        return {
            '.EntropicLine': {
                'stroke': 'orange',
                'stroke-width': 10,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
