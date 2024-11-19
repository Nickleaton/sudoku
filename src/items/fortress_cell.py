"""FortressCell."""

from src.glyphs.fortress_cell_glyph import FortressCellGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.simple_cell_reference import SimpleCellReference
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class FortressCell(SimpleCellReference):
    """Represents a fortress cell in a puzzle, where the digit must be greater than its orthogonal neighbors."""

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
            list[Rule]: A list containing the rule that the digit in a
                        fortress cell must be bigger than its orthogonal neighbors.
        """
        return [
            Rule(
                "Odd",
                1,
                "The digit in a fortress cell must be bigger than its orthogonal neighbours"
            )
        ]

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
            ".FortressCell": {
                "stroke": "black",
                "stroke-width": 3
            }
        }

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add a constraint ensuring the digit in the fortress cell is larger than its orthogonal neighbors.

        Args:
            solver (PulpSolver): The solver to which the constraint will be added.
        """
        cell = Coord(self.row, self.column)
        for offset in Direction.orthogonals():
            other = cell + offset
            if not self.board.is_valid_coordinate(other):
                continue
            solver.model += solver.values[self.row][self.column] >= solver.values[other.row][
                other.column] + 1, f"Fortress_{self.row}_{self.column}_{other.row}_{other.column}"

    def bookkeeping(self) -> None:
        """Update the bookkeeping for the FortressCell.

        Sets the impossibility of containing digits that cannot be valid for the fortress cell's constraints.
        """
        digit = 1
        coord = Coord(self.row, self.column)
        cell = Cell.make(self.board, self.row, self.column)
        for offset in Direction.orthogonals():
            other = coord + offset
            if not self.board.is_valid_coordinate(other):
                continue
            cell.book.set_impossible([digit])
            digit += 1
