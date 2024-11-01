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
    """ Collection of cells"""

    def __init__(self, board: Board) -> None:
        super().__init__(board, [])

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        return cls(board)

    @property
    def cells(self) -> List[Cell]:
        return [item for item in self.items if isinstance(item, Cell)]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.board!r})"

    def add_unique_constraint(self, solver: PulpSolver, optional: bool = False):
        # Use set of cells to cope with loops
        for digit in self.board.digit_range:
            total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in set(self.cells)])
            if optional:
                solver.model += total <= 1, f"{self.name}_Unique_{digit}"
            else:
                solver.model += total == 1, f"{self.name}_Unique_{digit}"

    def add_total_constraint(self, solver: PulpSolver, total: int) -> None:
        value = lpSum([solver.values[cell.row][cell.column] for cell in self.cells])
        solver.model += value == total, f"Total_{self.name}"

    def add_contains_constraint(self, solver: PulpSolver, digits: List[int]):
        for digit in digits:
            choice_total = lpSum([solver.choices[digit][cell.row][cell.column] for cell in self.cells])
            solver.model += choice_total == 1, f"{self.name}_Contains_{digit}"

    def add_sequence_constraint(self, solver: PulpSolver, order: Order):
        for i in range(1, len(self)):
            value1 = solver.values[self.cells[i - 1].row][self.cells[i - 1].column]
            value2 = solver.values[self.cells[i].row][self.cells[i].column]
            name = f"{order.name}_{self.cells[i - 1].name}_{self.cells[i].name}"
            if order == Order.INCREASING:
                solver.model += value1 + 1 <= value2, name
            else:
                solver.model += value1 >= value2 + 1, name

    def add_allowed_constraint(self, solver: PulpSolver, cells: List[Cell], allowed: List[int]):
        for cell in cells:
            cell.book.set_possible(allowed)

    def to_dict(self) -> Dict:
        return {self.__class__.__name__: None}

    @property
    def used_classes(self) -> Set[Type[Item]]:
        """
        Return a set of classes that this item uses.

        The set of classes is determined by traversing the method resolution
        order (MRO) of the item's class. The set contains all classes in the
        MRO, except for the abstract base class (`abc.ABC`) and the `object`
        class.

        Returns:
            Set[Type[Self]]: A set of classes that this item uses.
        """
        result = super().used_classes
        # Iterate over the cells in the region
        for cell in self.cells:
            # Add the used classes of the cell to the result
            result |= cell.used_classes
        return result
