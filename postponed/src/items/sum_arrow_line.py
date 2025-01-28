"""SumArrowLine."""
from collections import defaultdict

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from postponed.src.items.line import Line
from src.glyphs.arrow_line_glyph import ArrowLineGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.utils.functions import Functions
from src.utils.rule import Rule


class SumArrowLine(Line):
    """Represents an arrow line where digits along the line must sum to the digit at the starting (circle) cell.

    Digits on the arrow are allowed to repeat, and the total sum of digits
    along the arrow equals the number in the initial cell.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define the rules for the SumArrowLine.

        Returns:
            list[Rule]: A list of Rule objects specifying the arrow's summing requirement.
        """
        rule_text: str = 'Digits along an arrow must sum to the digit in its circle. Digits may repeat along an arrow.'
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Create start_location visual representation of the SumArrowLine.

        Returns:
            list[Glyph]: A list containing an `ArrowLineGlyph` for rendering.
        """
        return [ArrowLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells])]

    @property
    def tags(self) -> set[str]:
        """Tags associated with SumArrowLine.

        Returns:
            set[str]: Tags specific to SumArrowLine, combined with inherited tags.
        """
        return super().tags.union({self.__class__.__name__, 'Sum'})

    def css(self) -> dict:
        """CSS styling properties for rendering SumArrowLine.

        Returns:
            dict: A dictionary defining CSS properties for `.SumArrowLine` and its start_location and end_location points.
        """
        return {
            '.SumArrowLine': {
                'stroke': 'grey',
                'fill': 'white',
                'stroke-width': 3,
            },
            '.SumArrowLineStart': {
            },
            '.SumArrowLineEnd': {
                'fill-opacity': 0,
            },
        }

    def add_constraint(self, solver: PulpSolver) -> None:
        """Constrain the cells along the arrow so they sum to the number in the starting cell.

        Args:
            solver (PulpSolver): The Pulp solver instance to which constraints will be added.

        Returns:
            None
        """
        # Sum constraint: the sum of arrow cells must equal the starting cell number
        self.add_sum_constraint(solver)

        if len(self.cells) == 2:
            self.add_two_cell_constraint(solver)
            return

        regions = self.get_box_regions()
        self.add_minimum_sum_constraint(solver, regions)
        self.add_digit_value_constraints(solver)
        self.add_total_constraints(solver)

    def add_sum_constraint(self, solver: PulpSolver) -> None:
        """Set up a sum constraint where the sum of arrow cells must equal the starting cell number.

        Args:
            solver (PulpSolver): The Pulp solver instance to which the sum constraint will be added.
        """
        total = lpSum(
            [
                solver.variables.numbers[self.cells[index].row][self.cells[index].column]
                for index in range(1, len(self))
            ],
        )
        solver.model += total == solver.variables.numbers[self.cells[0].row][self.cells[0].column], self.name

    def add_two_cell_constraint(self, solver: PulpSolver) -> None:
        """Set up constraints to ensure that the two arrow cells match in target_value.

        Args:
            solver (PulpSolver): The Pulp solver instance to which the constraints will be added.
        """
        for digit in self.board.digit_range:
            cell0: Cell = self.cells[0]
            cell1: Cell = self.cells[1]
            d1 = solver.variables.choices[digit][cell0.row][cell0.column]
            d2 = solver.variables.choices[digit][cell1.row][cell1.column]
            solver.model += d1 == d2, f'{self.name}_one_cell_{digit}'

    def get_box_regions(self) -> dict[int, list[Cell]]:
        """Return a dictionary of box regions, mapping box indices to lists of cells.

        Returns:
            dict[int, list[Cell]]: A dictionary where keys are box indices, and cell_values are lists of `Cell` objects.
        """
        regions: defaultdict[int, list[Cell]] = defaultdict(list)
        for cell in self.cells:
            box = self.board.box_index(cell.row, cell.column)
            regions[box].append(cell)
        return dict(regions)

    def add_minimum_sum_constraint(self, solver: PulpSolver, regions: dict[int, list[Cell]]) -> None:
        """Set up a minimum sum constraint based on the smallest possible sum per box region.

        Args:
            solver (PulpSolver): The Pulp solver instance to which the minimum sum constraint will be added.
            regions (dict[int, list[Cell]]): A dictionary of box indices and their corresponding cells.
        """
        total = sum(Functions.triangular(len(cells)) for _, cells in regions.items())
        solver.model += solver.variables.numbers[self.cells[0].row][self.cells[0].column] >= total, f'{self.name}_head'

    def add_digit_value_constraints(self, solver: PulpSolver) -> None:
        """Set up constraints for digits where the digit target_value is less than the total sum.

        Args:
            solver (PulpSolver): The Pulp solver instance to which the digit target_value constraints will be added.
        """
        total = sum(Functions.triangular(len(cells)) for _, cells in self.get_box_regions().items())  # Calculate total
        for digit in self.board.digit_range:
            if digit >= total:
                continue
            start_cell: Cell = self.cells[0]
            choice = solver.variables.choices[digit][start_cell.row][start_cell.column]
            solver.model += choice == 0, f'{self.name}_{digit}_head'

    def add_total_constraints(self, solver: PulpSolver) -> None:
        """Set up constraints for the tail cells to limit possible digit cell_values.

        Args:
            solver (PulpSolver): The Pulp solver instance to which the tail constraints will be added.
        """
        total = sum(Functions.triangular(len(cells)) for _, cells in self.get_box_regions().items())  # Calculate total
        for index, cell in enumerate(self.cells[1:], start=1):
            for digit in self.board.digit_range:
                if digit <= self.board.maximum_digit - total + 1:
                    continue
                choice = solver.variables.choices[digit][cell.row][cell.column]
                solver.model += choice == 0, f'{self.name}_{index}_{digit}_tail'
