"""Quadro."""
from itertools import product

from pulp import lpSum

from src.board.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Quadro(Item):
    """Represents start 2*2 block of cells that enforces start parity rule on the digits.

    The rule states that there must be at least one even and one odd digit in every 2*2 adjacent cells.
    """

    minimum_count: int = 1
    maximum_count: int = 3

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with this Quadro.

        Returns:
            list[Rule]: A list containing the rule for the Quadro.
        """
        rule_text: str = 'There must be at least one even and at least one odd digit in every 2*2 adjacent cells'
        return [Rule('Quadro', 3, rule_text)]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start new Quadro instance for the given board.

        Args:
            board (Board): The board on which the Quadro is placed.
            yaml (dict): The YAML configuration (currently unused for this class).

        Returns:
            Item: A new Quadro instance.
        """
        return cls(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start new Quadro instance for the given board.

        Args:
            board (Board): The board on which the Quadro is placed.
            yaml_data (dict): The YAML configuration (currently unused for this class).

        Returns:
            Item: A new Quadro instance.
        """
        return cls.create(board, yaml_data)

    def __repr__(self) -> str:
        """Return start string representation of the Quadro instance.

        Returns:
            str: A string representing the Quadro instance with its board.
        """
        return f'{self.__class__.__name__}({self.board!r})'

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the parity constraints for the Quadro to the solver model.

        For each 2*2 block of cells, the constraint ensures there is at least one even and one odd digit.

        Args:
            solver (PulpSolver): The solver to which the constraints will be added.
        """
        offsets = (Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(1, 1))
        for row, column in product(self.board.row_range, self.board.column_range):
            if row == self.board.board_rows:
                continue
            if column == self.board.board_columns:
                continue
            evens = lpSum(
                [
                    Cell.make(self.board, int(row + offset.row), int(column + offset.column)).parity(solver)
                    for offset in offsets
                ],
            )
            # There are four cells. At least one must be even
            solver.model += evens >= Quadro.minimum_count, f'{self.name}_{row}_{column}_even'
            # There are four cells. At least one must be odd.
            # If there are 4 evens, it's wrong. So no more than 3 evens means at least one odd
            solver.model += evens <= Quadro.maximum_count, f'{self.name}_{row}_{column}_odd'
