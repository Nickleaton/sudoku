from typing import List, Dict, Set, Type

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.order import Order

REGION_TOTALS = False


class Region(ComposedItem):
    """Represents a collection of cells, enforcing various constraints on them."""

    def __init__(self, board: Board) -> None:
        """Initialize a Region on the given board.

        Args:
            board (Board): The Sudoku board associated with this region.
        """
        super().__init__(board, [])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a Region from YAML configuration.

        Args:
            board (Board): The board on which this region will be created.
            yaml (Dict): The YAML configuration for this region.

        Returns:
            Item: The instantiated Region.
        """
        return cls(board)

    @property
    def cells(self) -> List[Cell]:
        """Return the list of cells in the region.

        Returns:
            List[Cell]: List of cells that belong to this region.
        """
        return [item for item in self.items if isinstance(item, Cell)]

    def __repr__(self) -> str:
        """Return a string representation of the region.

        Returns:
            str: String representation of the region.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def add_unique_constraint(self, solver: PulpSolver, optional: bool = False):
        """Add a constraint to ensure each digit appears only once in the region.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
            optional (bool): Whether the constraint is optional. Defaults to False.
        """
        for digit in self.board.digit_range:
            total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in set(self.cells)])
            if optional:
                solver.model += total <= 1, f"{self.name}_Unique_{digit}"
            else:
                solver.model += total == 1, f"{self.name}_Unique_{digit}"

    def add_total_constraint(self, solver: PulpSolver, total: int) -> None:
        """Add a constraint to enforce a total sum of cell values within the region.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
            total (int): The required total sum for the values in the region.
        """
        value = lpSum([solver.values[cell.row][cell.column] for cell in self.cells])
        solver.model += value == total, f"Total_{self.name}"

    def add_contains_constraint(self, solver: PulpSolver, digits: List[int]):
        """Add constraints to ensure specified digits are present in the region.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
            digits (List[int]): The digits that must be included in the region.
        """
        for digit in digits:
            choice_total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in self.cells])
            solver.model += choice_total == 1, f"{self.name}_Contains_{digit}"

    def add_sequence_constraint(self, solver: PulpSolver, order: Order):
        """Add a sequence constraint to enforce an ordered sequence of values.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
            order (Order): The sequence order (e.g., INCREASING or DECREASING).
        """
        for i in range(1, len(self)):
            value1 = solver.values[self.cells[i - 1].row][self.cells[i - 1].column]
            value2 = solver.values[self.cells[i].row][self.cells[i].column]
            name = f"{order.name}_{self.cells[i - 1].name}_{self.cells[i].name}"
            if order == Order.INCREASING:
                solver.model += value1 + 1 <= value2, name
            else:
                solver.model += value1 >= value2 + 1, name

    def add_allowed_constraint(self, solver: PulpSolver, cells: List[Cell], allowed: List[int]):
        """Add constraints to restrict the allowed digits in specified cells.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
            cells (List[Cell]): List of cells to restrict.
            allowed (List[int]): List of allowed digits for the cells.
        """
        for cell in cells:
            cell.book.set_possible(allowed)

    def to_dict(self) -> Dict:
        """Serialize the region to a dictionary format.

        Returns:
            Dict: Dictionary representation of the region.
        """
        return {self.__class__.__name__: None}

    @property
    def used_classes(self) -> Set[Type[Item]]:
        """Return a set of classes used by this region and its cells.

        Returns:
            Set[Type[Item]]: Set of classes utilized within the region.
        """
        result = super().used_classes
        for cell in self.cells:
            result |= cell.used_classes
        return result
