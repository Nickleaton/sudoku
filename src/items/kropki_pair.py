"""KropkiPair."""
from itertools import product

from pulp import LpVariable, LpInteger, lpSum

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.kropki_glyph import KropkiGlyph
from src.items.cell import Cell
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class KropkiPair(Pair):
    """Represents a Kropki dot pair in a puzzle.

    Two cells where one of the cells is exactly twice the value other.
    """

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell):
        """Initialize a KropkiPair with two cells and an empty SOS dictionary.

        Args:
            board (Board): The board instance this pair is part of.
            cell_1 (Cell): The first cell in the pair.
            cell_2 (Cell): The second cell in the pair.
        """
        super().__init__(board, cell_1, cell_2)
        self.sos: dict[int, LpVariable] = {}

    @property
    def factor(self) -> int:
        """Get the multiplication factor associated with this pair.

        Returns:
            int: The factor by which one cell's value must be a multiple of the other.
        """
        return 2

    @property
    def factor_name(self) -> str:
        """Get the name of the factor.

        Returns:
            str: The name of the factor.
        """
        return "double"

    @property
    def rules(self) -> list[Rule]:
        """Define the rule for the Kropki pair.

        Returns:
            list[Rule]: A list of rules for the Kropki pair.
        """
        return [
            Rule(
                self.__class__.__name__,
                1,
                (
                    f"A black dot between two cells means that one of the digits in those cells "
                    f"is exactly {self.factor_name} the other"
                )
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Generate glyph representations for the Kropki pair.

        Returns:
            list[Glyph]: A list of glyphs representing the Kropki pair.
        """
        return [KropkiGlyph(self.__class__.__name__, self.cell_1.coord.center, self.cell_2.coord.center)]

    @property
    def tags(self) -> set[str]:
        """Tags associated with the Kropki pair.

        Returns:
            set[str]: A set of tags for the Kropki pair.
        """
        return super().tags.union({'Kropki'})

    def valid(self, x: int, y: int) -> bool:
        """Check if two digits conform to the Kropki pair rule.

        Args:
            x (int): The first digit.
            y (int): The second digit.

        Returns:
            bool: True if one of the digits is exactly `factor` times the other.
        """
        return x == self.factor * y or self.factor * x == y

    def possible(self) -> set:
        """Determine possible digits that satisfy the Kropki pair rule.

        Returns:
            set: A set of digits that satisfy the rule.
        """
        used = set({})
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if self.valid(x, y):
                used.add(x)
                used.add(y)
        return used

    # pylint: disable=loop-invariant-statement
    def add_impossible_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for impossible digits in the pair cells.

        Args:
            solver (PulpSolver): The solver instance to which constraints are added.
        """
        for digit in set(self.board.digit_range) - self.possible():
            name = f"{self.name}_Impossible_kropki_pair_1_{digit}_{self.cell_1.row}_{self.cell_1.column}"
            solver.model += solver.choices[digit][self.cell_1.row][self.cell_1.column] == 0, name
            name = f"{self.name}_Impossible_kropki_pair_2_{digit}_{self.cell_2.row}_{self.cell_2.column}"
            solver.model += solver.choices[digit][self.cell_2.row][self.cell_2.column] == 0, name

    # pylint: disable=loop-invariant-statement
    def add_implausible_constraint(self, solver: PulpSolver) -> None:
        """Add constraints to restrict invalid digit pairs.

        Args:
            solver (PulpSolver): The solver instance to which constraints are added.
        """
        for x, y in product(self.board.digit_range, self.board.digit_range):
            choice1 = solver.choices[x][self.cell_1.row][self.cell_1.column]
            choice2 = solver.choices[y][self.cell_2.row][self.cell_2.column]
            if not self.valid(x, y):
                solver.model += choice1 + choice2 <= 1, f"{self.name}_Implausible_{x}_{y}"

    @property
    def count(self) -> int:
        """Count the valid digit pairs that meet the Kropki pair rule.

        Returns:
            int: The count of valid digit pairs.
        """
        count = 0
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if self.valid(x, y):
                count += 1
        return count

    def create_sos(self, solver: PulpSolver) -> None:
        """Create a set of special ordered sets (SOS) constraints.

        Args:
            solver (PulpSolver): The solver instance to which constraints are added.
        """
        sos_range = range(self.count)
        self.sos = LpVariable.dicts(self.name, sos_range, 0, 1, LpInteger)
        solver.model += lpSum([self.sos[i] for i in sos_range]) == 1, f"{self.name}_SOS"

    def add_unique_constraints(self, solver: PulpSolver) -> None:
        """Add constraints ensuring that valid pairs are uniquely enforced.

        Args:
            solver (PulpSolver): The solver instance to which constraints are added.
        """
        count = 0
        for x, y in product(self.board.digit_range, self.board.digit_range):
            if not self.valid(x, y):
                continue
            choice1 = solver.choices[x][self.cell_1.row][self.cell_1.column]
            choice2 = solver.choices[y][self.cell_2.row][self.cell_2.column]
            solver.model += choice1 + choice2 + (1 - self.sos[count]) <= 2, f"{self.name}_Valid_{x}_{y}"
            count += 1

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add all constraints necessary for the Kropki pair rule.

        Args:
            solver (PulpSolver): The solver instance to which constraints are added.
        """
        self.add_impossible_constraint(solver)
        self.add_implausible_constraint(solver)
        self.create_sos(solver)
        self.add_unique_constraints(solver)

    def css(self) -> dict:
        """Define CSS styling properties for rendering the Kropki pair.

        Returns:
            dict: A dictionary of CSS properties for the Kropki pair.
        """
        return {
            '.KropkiPair': {
                'fill': 'black',
                'stroke-width': 1,
                'stroke': 'black',
                'background': 'transparent'
            }
        }
