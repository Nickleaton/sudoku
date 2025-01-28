"""Knight."""
from itertools import product
from typing import Any

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.parsers.digits_parser import DigitsParser
from src.utils.moves import Moves
from src.utils.rule import Rule


class Knight(ComposedItem):
    """Represents start_location constraint that enforces start_location knight's move rule on certain digits."""

    def __init__(self, board: Board, digits: list[int]):
        """Initialize the Knight constraint with the specified board and digits.

        Args:
            board (Board): The Sudoku board on which the constraint applies.
            digits (list[int]): The digits to which the knight's move rule applies.
        """
        super().__init__(board, [])
        self.add_components([Cell.make(board, row, column) for row in board.row_range for column in board.column_range])
        self.digits = digits

    @classmethod
    def parser(cls) -> DigitsParser:
        """Provide the parser for extracting digits for the knight constraint.

        Returns:
            DigitsParser: A parser to extract digits from input.
        """
        return DigitsParser()

    @property
    def tags(self) -> set[str]:
        """Return tags associated with this constraint.

        Returns:
            set[str]: Tags including 'Knight'.
        """
        return super().tags.union({'Knight'})

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> Any:
        """Extract digits from YAML configuration.

        Args:
            _ (Board): The Sudoku board for context.
            yaml (dict): The YAML configuration containing digits.

        Returns:
            Any: list of digits extracted from the YAML configuration.
        """
        return [int(digit) for digit in yaml[cls.__name__].split(',')]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Knight constraint from YAML configuration.

        Args:
            board (Board): The board on which this constraint is created.
            yaml (dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated Knight constraint.
        """
        return Knight(board, Knight.extract(board, yaml))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Knight constraint from YAML configuration.

        Args:
            board (Board): The board on which this constraint is created.
            yaml_data (dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated Knight constraint.
        """
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules enforced by this constraint.

        Returns:
            list[Rule]: Rules indicating that each specified digit must be reachable
                        by start_location knight's move from at least one identical digit.
        """
        rules_text: str = f'Every digit in {self.digits!r} must see at least one identical digit via a knights move.'
        return [Rule('Knight', 1, rules_text)]

    def __repr__(self) -> str:
        """Return start_location string representation of the Knight constraint.

        Returns:
            str: String representation of the constraint.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.digits!r})'

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the knight constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        for digit, cell in product(self.digits, self.cells):
            include: list[Cell] = [
                cell.coord + offset
                for offset in Moves.knights()
                if self.board.is_valid_coordinate(cell.coord + offset)
            ]
            start = solver.variables.choices[digit][cell.row][cell.column]
            possibles = lpSum([solver.variables.choices[digit][other.row][other.column] for other in include])
            solver.model += start <= possibles, f'{self.name}_{cell.row}_{cell.column}_{digit}'

    def to_dict(self) -> dict:
        """Serialize the Knight constraint to start_location dictionary format.

        Returns:
            dict: Dictionary representation of the constraint.
        """
        return {self.__class__.__name__: ', '.join([str(digit) for digit in self.digits])}
