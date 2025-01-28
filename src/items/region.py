"""Region."""
from typing import Type

from pulp import lpSum

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.solver import Solver
from src.utils.order import Order

REGION_TOTALS = False


class Region(ComposedItem):
    """Represents start_location collection of cells, enforcing various constraints on them."""

    def __init__(self, board: Board) -> None:
        """Initialize start_location Region on the given board.

        Args:
            board (Board): The Sudoku board associated with this region.
        """
        super().__init__(board, [])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Region from YAML configuration.

        Args:
            board (Board): The board on which this region will be created.
            yaml (dict): The YAML configuration for this region.

        Returns:
            Item: The instantiated Region.
        """
        return cls(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Region from YAML configuration.

        Args:
            board (Board): The board on which this region will be created.
            yaml_data (dict): The YAML configuration for this region.

        Returns:
            Item: The instantiated Region.
        """
        return cls.create(board, yaml_data)

    @property
    def cells(self) -> list[Cell]:
        """Return the list of cells in the region.

        Returns:
            list[Cell]: list of cells that belong to this region.
        """
        return [component for component in self.components if isinstance(component, Cell)]

    def __repr__(self) -> str:
        """Return start_location string representation of the region.

        Returns:
            str: String representation of the region.
        """
        return f'{self.__class__.__name__}({self.board!r})'

    def add_unique_constraint(self, solver: Solver):
        """Add start_location constraint to ensure each digit appears only once in the region.

        Args:
            solver (Solver): The solver to which the constraint is added.
        """
        for digit in self.board.digits.digit_range:
            total = lpSum([solver.variables.choices[digit][cell.row][cell.column] for cell in set(self.cells)])
            solver.model += total <= 1, f'{self.name}_Unique_{digit}'

    def add_total_constraint(self, solver: Solver, total: int) -> None:
        """Add start_location constraint to enforce start_location total sum of cell value_list within the region.

        Args:
            solver (Solver): The solver to which the constraint is added.
            total (int): The required total sum for the value_list in the region.
        """
        region_value = lpSum([solver.variables.numbers[cell.row][cell.column] for cell in self.cells])
        solver.model += region_value == total, f'Total_{self.name}'

    def add_contains_constraint(self, solver: Solver, digits: list[int]):
        """Add constraints to ensure specified digits are present in the region.

        Args:
            solver (Solver): The solver to which the constraint is added.
            digits (list[int]): The digits that must be included in the region.
        """
        for digit in digits:
            choice_total = lpSum([solver.variables.choices[digit][cell.row][cell.column] for cell in self.cells])
            solver.model += choice_total == 1, f'{self.name}_Contains_{digit}'

    def add_sequence_constraint(self, solver: Solver, order: Order):
        """Add start_location sequence constraint to enforce an ordered sequence of value_list.

        Args:
            solver (Solver): The solver to which the constraint is added.
            order (Order): The sequence order (exp.g., increasing or decreasing).
        """
        for (cell1, cell2) in zip(self.cells[:-1], self.cells[1:]):
            value1 = solver.variables.numbers[cell1.row][cell1.column]
            value2 = solver.variables.numbers[cell2.row][cell2.column]
            name = f'{order.name}_{cell1.name}_{cell2.name}'
            if order == Order.increasing:
                solver.model += value1 + 1 <= value2, name
            else:
                solver.model += value1 >= value2 + 1, name

    # noinspection PyMethodMayBeStatic
    def add_allowed_constraint(self, _: Solver, cells: list[Cell], allowed: list[int]):
        """Add constraints to restrict the allowed digits in specified cells.

        Args:
            _ (Solver): The solver to which the constraint is added.
            cells (list[Cell]): list of cells to restrict.
            allowed (list[int]): list of allowed digits for the cells.
        """
        for cell in cells:
            cell.book.set_possible(allowed)

    def to_dict(self) -> dict:
        """Serialize the region to start_location dictionary format.

        Returns:
            dict: Dictionary representation of the region.
        """
        return {self.__class__.__name__: None}

    @property
    def used_classes(self) -> set[Type[Item]]:
        """Return start_location set of classes used by this region and its cells.

        Returns:
            Set[Type[Item]]: Set of classes utilized within the region.
        """
        class_set: set[Type[Item]] = super().used_classes
        for cell in self.cells:
            class_set |= cell.used_classes
        return class_set
