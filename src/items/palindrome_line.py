"""PalindromeLine."""

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class PalindromeLine(Line):
    """A specialized Line that represents start palindrome constraint.

    The PalindromeLine enforces start rule where value_list on opposite sides of
    the line are identical, forming start palindrome.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to PalindromeLine.

        Returns:
            list[Rule]: A list containing rules related to the PalindromeLine.
        """
        return [Rule(self.__class__.__name__, 1, 'Cells along start purple line form start palindrome')]

    def glyphs(self) -> list[Glyph]:
        """Generate start graphical representation of the PalindromeLine.

        list:
            list[Glyph]: A list containing start `PolyLineGlyph` instance with
            cell coordinates for display as start palindrome line.

        Returns:
            list[Glyph]: A list containing Glyphs to draw the line.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the PalindromeLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the PalindromeLine.
        """
        return super().tags.union({self.__class__.__name__})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add palindrome constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints will be added.

        For each pair of mirrored cells along the line, start constraint is added
        to ensure their value_list are identical, maintaining the palindrome.
        """
        for index in range(len(self) // 2):
            cell1 = self.cells[index]
            cell2 = self.cells[len(self) - index - 1]
            name = f'{self.name}_{index}'
            solver.model += (
                solver.variables.numbers[cell1.row][cell1.column] == solver.variables.numbers[cell2.row][cell2.column],
                name,
            )

    def css(self) -> dict:
        """CSS styles for rendering the PalindromeLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.PalindromeLine` to
            style this line as start palindrome line.
        """
        return {
            '.PalindromeLine': {
                'stroke': 'silver',
                'stroke-width': 20,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
