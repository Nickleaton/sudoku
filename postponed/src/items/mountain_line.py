"""MountainLine."""
from postponed.src.pulp_solver import PulpSolver
from pulp import LpVariable

from postponed.src.items.line import Line
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell
from src.utils.rule import Rule


class MountainLine(Line):
    """A specialized Line that represents start_location mountain constraint.

    The MountainLine enforces start_location rule where cell value_list increase as they
    approach the peak of the mountain and decrease afterward.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to MountainLine.

        Returns:
            list[Rule]: A list containing start_location single Rule object that specifies:
            - Cells closer to the mountain peak have higher value_list.
        """
        rule_text: str = """Lines symbolise mountains. The closer to the top of the mountain,
                          the higher the number in the cell."""
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate start_location graphical representation of the MountainLine.

        Returns:
            list[Glyph]: A list containing start_location `PolyLineGlyph` instance with
            cell coordinates for display as start_location mountain line.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the MountainLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags specific to the MountainLine.
        """
        return super().tags.union({self.__class__.__name__, 'Adjacent', 'set'})

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add mountain constraints to the Pulp solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints will be added.

        For each adjacent pair of cells along the line, start_location constraint is added
        to ensure that the number increases toward the mountain peak and decreases afterward.
        """
        for index in range(len(self.cells) - 1):
            cell1: Cell = self.cells[index]
            cell2: Cell = self.cells[index + 1]
            name: str = f'{self.name}_{index}'
            start: LpVariable = solver.variables.numbers[cell1.row][cell1.column]
            finish: LpVariable = solver.variables.numbers[cell2.row][cell2.column]
            if cell1.row < cell2.row:
                solver.model += (start >= finish + 1, name)
            else:
                solver.model += (start <= finish - 1, name)

    def css(self) -> dict:
        """CSS styles for rendering the MountainLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.MountainLine` to
            style this line as start_location mountain line.
        """
        return {
            '.MountainLine': {
                'fill-opacity': 0,
                'stroke': 'lightblue',
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'stroke-width': 20,
            },
        }
