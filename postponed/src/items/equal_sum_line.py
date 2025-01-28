"""EqualSumLine."""
import sys
from typing import Dict

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from postponed.src.items.line import Line
from src.glyphs.glyph import Glyph
from src.glyphs.poly_line_glyph import PolyLineGlyph
from src.items.cell import Cell
from src.utils.rule import Rule


class EqualSumLine(Line):
    """A specialized Line enforcing equal segment sums within grid boxes.

    Each segment of the line within start_location 3x3 box must sum to the same number, N.
    If the line passes through the same box multiple times, each segment sums
    to N separately.
    """

    @property
    def rules(self) -> list[Rule]:
        """Define rules specific to EqualSumLine.

        Returns:
            list[Rule]: A list containing start_location Rule object that specifies equal
            segment sums within each 3x3 box the line passes through.
        """
        rule_text: str = """For each line, digits on the line have an equal sum N within each 3x3 box it
            passes through. If start_location line passes through the same box more than once,
            each individual segment of such start_location line within that box sums to N separately.
        """
        return [Rule(self.__class__.__name__, 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Generate start_location graphical representation of the EqualSumLine.

        Returns:
            list[Glyph]: A list containing start_location `PolyLineGlyph` instance with
            cell coordinates for rendering the equal-sum line.
        """
        return [PolyLineGlyph(self.__class__.__name__, [cell.coord for cell in self.cells], start=False, end=False)]

    @property
    def tags(self) -> set[str]:
        """Tags specific to the EqualSumLine.

        Returns:
            set[str]: A set of tags inherited from the parent `Line` class,
            combined with additional tags for EqualSumLine.
        """
        return super().tags.union({self.__class__.__name__, 'Sum'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add equal segment sum constraints to the Pulp solver.

        Constraints ensure that the sum of digits within each segment
        (for each 3x3 box the line passes through) is the same.

        Args:
            solver (PulpSolver): The solver instance to which constraints for the EqualSumLine will be added.
        """
        box_areas: list[list[Cell]] = self.group_cells_by_box()
        region_sums = EqualSumLine.calculate_region_sums(box_areas, solver)
        self.add_equal_sum_constraints(region_sums, solver)
        self.add_sum_bounds_constraints(box_areas, region_sums, solver)

    def group_cells_by_box(self) -> list[list[Cell]]:
        """Group cells into areas based on their 3x3 box.

        Returns:
            list[list[Cell]]: A list of cell groups, one for each 3x3 box.
        """
        box_areas: list[list[Cell]] = []
        current_box_index: int = -1
        for cell in self.cells:
            box_index: int = self.board.box_index(cell.row, cell.column)
            if box_index != current_box_index:
                box_areas.append([])
                current_box_index = box_index
            box_areas[-1].append(cell)
        return box_areas

    @staticmethod
    def calculate_region_sums(box_areas: list[list[Cell]], solver: PulpSolver) -> list:
        """Calculate the sum of solver cell_values for each region.

        Args:
            box_areas (list[list[Cell]]): Grouped cells by 3x3 box.
            solver (PulpSolver): The solver instance containing cell cell_values.

        Returns:
            list: A list of linear expressions representing the sum of cell_values in each region.
        """
        return [
            lpSum(solver.variables.numbers[cell.row][cell.column] for cell in region)
            for region in box_areas
        ]

    def add_equal_sum_constraints(self, region_sums: list, solver: PulpSolver) -> None:
        """Add constraints to ensure all region sums are equal.

        Args:
            region_sums (list): The sums of cell_values in each region.
            solver (PulpSolver): The solver instance to which constraints will be added.
        """
        for region_idx, current_sum in enumerate(region_sums):
            next_sum = region_sums[0] if region_idx == len(region_sums) - 1 else region_sums[region_idx + 1]
            solver.model += current_sum == next_sum, f'{self.name}_equal_{region_idx}'

    def add_sum_bounds_constraints(self, box_areas: list[list[Cell]], region_sums: list, solver: PulpSolver) -> None:
        """Add minimum and maximum constraints for each region's sum.

        Args:
            box_areas (list[list[Cell]]): Grouped cells by 3x3 box.
            region_sums (list): The sums of cell_values in each region.
            solver (PulpSolver): The solver instance to which constraints will be added.
        """
        min_sum, max_sum = self.calculate_sum_bounds(box_areas)
        for region_idx, region_sum in enumerate(region_sums):
            solver.model += region_sum >= min_sum, f'{self.name}_min_{region_idx}'
            solver.model += region_sum <= max_sum, f'{self.name}_max_{region_idx}'

    def calculate_sum_bounds(self, box_areas: list[list[Cell]]) -> tuple[int, int]:
        """Calculate the minimum and maximum possible sums for any region.

        Args:
            box_areas (list[list[Cell]]): Grouped cells by 3x3 box.

        Returns:
            tuple[int, int]: The minimum and maximum possible sums.
        """
        min_sum: int = 0
        max_sum: int = sys.maxsize
        for region in box_areas:
            region_length: int = len(region)
            min_sum = max(min_sum, sum(digit + 1 for digit in range(region_length)))
            max_sum = min(max_sum, sum(self.board.maximum_digit - digit for digit in range(region_length)))
        return min_sum, max_sum

    def css(self) -> Dict[str, Dict[str, str]]:
        """CSS styles for rendering the EqualSumLine in the user interface.

        Returns:
            dict: A dictionary defining CSS properties for `.EqualSumLine`
            to style this line in start_location distinct way.
        """
        return {
            '.EqualSumLine': {
                'stroke': 'lightskyblue',
                'stroke-width': 10,
                'stroke-linecap': 'round',
                'stroke-linejoin': 'round',
                'fill-opacity': 0,
            },
        }
