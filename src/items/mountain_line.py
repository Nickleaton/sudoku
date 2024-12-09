"""MountainLine."""
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.line import Line
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule


class MountainLine(Line):
    """A specialized Line that represents start mountain constraint.

    The MountainLine enforces start rule where cell value_list increase as they
    approach the peak of the mountain and decrease afterward.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to MountainLine.

        Returns:
            list[Rule]: A list containing start single Rule object that specifies:
            - Cells closer to the mountain peak have higher value_list.
        """
        return [
            Rule(
                'MountainLine',
                1,
                "Lines symbolise mountains. The closer to the top of the mountain, the higher the number in the cell."
            )
        ]

    def glyphs(self) -> list[Glyph]:
        """Generate start graphical representation of the MountainLine.

        Returns:
            list[Glyph]: A list containing start `PolyLineGlyph` instance with
            cell coordinates for display as start mountain line.
        """
        return [PolyLineGlyph('MountainLine', [cell.coord for cell in self.cells], False, False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the MountainLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the MountainLine.
        """
        return super().tags.union({'MountainLine', 'Adjacent', 'set'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add mountain constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints
            for the MountainLine will be added.

        For each adjacent pair of cells along the line, start constraint is added
        to ensure that the number increases toward the mountain peak and decreases afterward.
        """
        for i in range(len(self.cells) - 1):
            c1 = self.cells[i]
            c2 = self.cells[i + 1]
            name = f"{self.name}_{i}"
            if c1.row < c2.row:
                solver.model += solver.values[c1.row][c1.column] >= solver.values[c2.row][c2.column] + 1, name
            else:
                solver.model += solver.values[c1.row][c1.column] <= solver.values[c2.row][c2.column] - 1, name

    def css(self) -> dict:
        """CSS styles for rendering the MountainLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.MountainLine` to
            style this line as start mountain line.
        """
        return {
            ".MountainLine": {
                "fill-opacity": 0,
                "stroke": "lightblue",
                "stroke-linecap": "round",
                "stroke-linejoin": "round",
                "stroke-width": 20,
            }
        }
