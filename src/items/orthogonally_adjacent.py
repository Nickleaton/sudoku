"""OrthogonallyAdjacent."""

from itertools import product

from src.board.board import Board
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class OrthogonallyAdjacent(ComposedItem):
    """Represents a constraint where consecutive digits are restricted from being orthogonally adjacent."""

    def __init__(self, board: Board):
        """Initialize the OrthogonallyAdjacent constraint on the given board.

        Args:
            board (Board): The Sudoku board to which the constraint applies.
        """
        super().__init__(board, [])

    @property
    def tags(self) -> set[str]:
        """Get the set of tags associated with this constraint.

        Returns:
            set[str]: A set of tags, including 'OrthogonallyAdjacent'.
        """
        return super().tags.union({'OrthogonallyAdjacent'})

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an OrthogonallyAdjacent constraint from a YAML configuration.

        Args:
            board (Board): The board on which the constraint is created.
            yaml (dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated OrthogonallyAdjacent constraint.
        """
        return OrthogonallyAdjacent(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an OrthogonallyAdjacent constraint from a YAML configuration (alternative method).

        Args:
            board (Board): The board on which the constraint is created.
            yaml_data (dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated OrthogonallyAdjacent constraint.
        """
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Get the list of rules enforced by this constraint.

        Returns:
            list[Rule]: A list of rules indicating that consecutive digits must never be orthogonally adjacent.
        """
        return [
            Rule('OrthogonallyAdjacent', 1, 'Consecutive digits must never be orthogonally adjacent'),
        ]

    def __repr__(self) -> str:
        """Return a string representation of the OrthogonallyAdjacent constraint.

        Returns:
            str: A string representation of the constraint.
        """
        return f'{self.__class__.__name__}({self.board!r})'

    def to_dict(self) -> dict:
        """Serialize the OrthogonallyAdjacent constraint to a dictionary format.

        Returns:
            dict: A dictionary representation of the constraint.
        """
        return {self.__class__.__name__: None}

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the orthogonally adjacent constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        for row, column in product(self.board.row_range, self.board.row_range):
            for offset in Moves.orthogonals():
                # Skip invalid cells
                if not self.board.is_valid(int(row + offset.row), int(column + offset.column)):
                    continue

                # Add constraints for adjacent digits
                self._add_adjacent_constraints(solver, row, column, offset)

    def _add_adjacent_constraints(self, solver: PulpSolver, row: int, column: int, offset: Coord) -> None:
        """Add constraints for adjacent digits.

        Args:
            solver (PulpSolver): The solver to which the constraints are added.
            row (int): The current row index.
            column (int): The current column index.
            offset (Coord): The offset for orthogonal directions.
        """
        for digit in range(1, self.board.maximum_digit):
            lhs = solver.variables.choices[digit][row][column]
            prefix = f'{self.name}_{row}_{column}_{row + offset.row}_{column + offset.column}_{digit}'

            for adj_digit in (digit - 1, digit + 1):
                if 1 <= adj_digit <= self.board.maximum_digit:
                    rhs = solver.variables.choices[adj_digit][row + offset.row][column + offset.column]
                    solver.model += lhs + rhs <= 1, f'{prefix}_{adj_digit}'
