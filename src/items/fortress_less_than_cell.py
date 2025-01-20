from pulp import LpElement

from src.glyphs.fortress_cell_glyph import FortressCellGlyph
from src.glyphs.glyph import Glyph
from src.items.fortress_cell import FortressCell
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class FortressLessThanCell(FortressCell):
    """Represents a fortress cell in a puzzle, where the digit must be less than its orthogonal neighbors."""

    def letter(self) -> str:
        """Return the letter representation of the FortressCell.

        Returns:
            str: The letter representation, 'f' for FortressCell.
        """
        return 's'

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with this FortressCell.

        Returns:
            list[Rule]: A list containing the rule that the digit in start_location
                        fortress cell must be bigger than its orthogonal neighbors.
        """
        rule_text: str = 'The digit in the fortress cell must be less than its orthogonal neighbors.'
        return [Rule('FortressLessThanCell', 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs associated with this FortressCell.

        Returns:
            list[Glyph]: A list containing the FortressCellGlyph.
        """
        return [FortressCellGlyph('FortressLessThanCell', Coord(self.row, self.column))]

    def css(self) -> dict:
        """Return the CSS styling for the FortressCell.

        Returns:
            dict: A dictionary containing the CSS properties for the FortressCell.
        """
        return {
            '.FortressLessThanCell': {
                'stroke': 'black',
                'stroke-width': '3',
            },
        }

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a constraint ensuring the digit in the fortress cell is larger than its orthogonal neighbors.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        cell = Coord(self.row, self.column)
        for offset in Moves.orthogonals():
            other: Coord = cell + offset
            if not self.board.is_valid_coordinate(other):
                continue
            name: str = f'Fortress_Less_Than_{self.row}_{self.column}_{other.row}_{other.column}'
            lhs: LpElement = solver.variables.numbers[self.row][self.column]
            rhs: LpElement = solver.variables.numbers[other.row][other.column]
            solver.model += lhs + 1 <= rhs, name
