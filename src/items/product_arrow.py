"""ProductArrow."""

from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.glyphs.glyph import Glyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class ProductArrowLine(Line):
    """A specialized Line that represents a product constraint on an arrow.

    The ProductArrowLine enforces a rule where digits along the arrow line,
    when multiplied together, should equal the digit in the circle at the end
    of the arrow. Digits may repeat if other rules allow it.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to ProductArrowLine.

        Returns:
            list[Rule]: A list containing a single Rule object that specifies:
            - Digits along an arrow, when multiplied, should equal the circle's digit.
            - Digits may repeat along the arrow if other rules allow.
        """
        return [
            Rule(
                'Arrow',
                1,
                "Digits along an arrow, when multiplied together will give the digit in its circle. "
                "Digits may repeat along an arrow if allowed by other rules."
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Generate graphical representation of the ProductArrowLine.

        Returns:
            list[Glyph]: A list containing an `ArrowLineGlyph` instance with
            cell coordinates for display as an arrow line.
        """
        return [ArrowLineGlyph('Arrow', [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the ProductArrowLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the ProductArrowLine.
        """
        return super().tags.union({'Arrow', 'Product'})

    def css(self) -> dict:
        """CSS styles for rendering the ProductArrowLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.Arrow`, `.ArrowStart`,
            and `.ArrowEnd` classes used to style this arrow line visually.
        """
        return {
            '.Arrow': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3
            },
            '.ArrowStart': {
            },
            '.ArrowEnd': {
                'fill-opacity': 0
            }
        }

    # TODO: Implement the constraint logic for the ProductArrowLine
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add product constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints
            for the ProductArrowLine will be added.

        Note:
            This method is currently not implemented.
        """
