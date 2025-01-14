"""FortressCell."""
from pulp import LpElement

from src.glyphs.fortress_cell_glyph import FortressCellGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.simple_cell_reference import SimpleCellReference
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class FortressCell(SimpleCellReference):
    """Represents start fortress cell in start puzzle, where the digit must be greater than its orthogonal neighbors."""

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
            list[Rule]: A list containing the rule that the digit in start
                        fortress cell must be bigger than its orthogonal neighbors.
        """
        rule_text: str = 'The digit in the fortress cell must be bigger than its orthogonal neighbors.'
        return [Rule('FortressCell', 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate the glyphs associated with this FortressCell.

        Returns:
            list[Glyph]: A list containing the FortressCellGlyph.
        """
        return [FortressCellGlyph('FortressCell', Coord(self.row, self.column))]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with this FortressCell.

        Returns:
            set[str]: A set of tags including 'Comparison'.
        """
        return super().tags.union({'Comparison'})

    def css(self) -> dict:
        """Return the CSS styling for the FortressCell.

        Returns:
            dict: A dictionary containing the CSS properties for the FortressCell.
        """
        return {
            '.FortressCell': {
                'stroke': 'black',
                'stroke-width': '3',
            },
        }

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add start constraint ensuring the digit in the fortress cell is larger than its orthogonal neighbors.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        cell = Coord(self.row, self.column)
        for offset in Moves.orthogonals():
            other = cell + offset
            if not self.board.is_valid_coordinate(other):
                continue
            name: str = f'Fortress_{self.row}_{self.column}_{other.row}_{other.column}'
            lhs: LpElement = solver.variables.numbers[self.row][self.column]
            rhs: LpElement = solver.variables.numbers[other.row][other.column]
            solver.model += lhs >= rhs + 1, name

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the FortressCell.

        Sets the impossibility of containing digits that cannot be valid for the fortress cell's constraints.
        """
        digit = 1
        coord = Coord(self.row, self.column)
        cell = Cell.make(self.board, self.row, self.column)
        for offset in Moves.orthogonals():
            other = coord + offset
            if not self.board.is_valid_coordinate(other):
                continue
            cell.book.set_impossible([digit])
            digit += 1
