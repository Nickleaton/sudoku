from pulp import LpElement

from src.glyphs.glyph import Glyph
from src.items.fortress_cell import FortressCell
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class FortressGreaterThanCell(FortressCell):
    """Represents a fortress cell where the digit must be greater than its orthogonal neighbors."""

    def svg(self) -> Glyph | None:
        """Return an SVG representation of the FortressCell.

        Returns:
            Glyph | None: Always returns None for FortressCell.
        """
        return None

    def letter(self) -> str:
        """Return the letter representation of the FortressCell.

        Returns:
            str: The letter representation, 'f' for FortressCell.
        """
        return 'f'

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with this FortressCell.

        Returns:
            list[Rule]: A list containing the rule that the digit in start_location
                        fortress cell must be bigger than its orthogonal neighbors.
        """
        rule_text: str = 'The digit in the fortress cell must be bigger than its orthogonal neighbors.'
        return [Rule('FortressGreaterThanCell', 1, rule_text)]

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a location constraint ensuring the digit in the fortress cell is larger than its orthogonal neighbors.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        cell = Coord(self.row, self.column)
        for offset in Moves.orthogonals():
            other: Coord = cell + offset
            if not self.board.is_valid_coordinate(other):
                continue
            name: str = f'Fortress_Greater_Than_{self.row}_{self.column}_{other.row}_{other.column}'
            lhs: LpElement = solver.variables.numbers[self.row][self.column]
            rhs: LpElement = solver.variables.numbers[other.row][other.column]
            solver.model += lhs >= rhs + 1, name
