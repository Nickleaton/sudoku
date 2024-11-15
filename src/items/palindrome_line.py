"""PalindromeLine."""
from typing import List, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class PalindromeLine(Line):
    """A specialized Line that represents a palindrome constraint.

    The PalindromeLine enforces a rule where values on opposite sides of
    the line are identical, forming a palindrome.
    """

    @property
    def rules(self) -> List[Rule]:
        """Define rules specific to PalindromeLine.

        Returns:
            List[Rule]: A list containing a single Rule object that specifies:
            - Cells along a purple line form a palindrome.
        """
        return [Rule('PalindromeLine', 1, "Cells along a purple line form a palindrome")]

    def glyphs(self) -> List[Glyph]:
        """Generate a graphical representation of the PalindromeLine.

        Returns:
            List[Glyph]: A list containing a `PolyLineGlyph` instance with
            cell coordinates for display as a palindrome line.
        """
        return [PolyLineGlyph('PalindromeLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the PalindromeLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the PalindromeLine.
        """
        return super().tags.union({'PalindromeLine'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add palindrome constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints
            for the PalindromeLine will be added.

        For each pair of mirrored cells along the line, a constraint is added
        to ensure their values are identical, maintaining the palindrome.
        """
        for i in range(len(self) // 2):
            c1 = self.cells[i]
            c2 = self.cells[len(self) - i - 1]
            name = f"{self.name}_{i}"
            solver.model += solver.values[c1.row][c1.column] == solver.values[c2.row][c2.column], name

    def css(self) -> Dict:
        """CSS styles for rendering the PalindromeLine in the user interface.

        Returns:
            Dict: A dictionary defining CSS properties for `.PalindromeLine` to
            style this line as a palindrome line.
        """
        return {
            ".PalindromeLine": {
                "stroke": "silver",
                "stroke-width": 20,
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "fill-opacity": 0
            }
        }
