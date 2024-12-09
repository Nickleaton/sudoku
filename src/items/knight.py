"""Knight."""
from typing import Any

from pulp import lpSum

from src.board.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.parsers.digits_parser import DigitsParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class Knight(ComposedItem):
    """Represents start constraint that enforces start knight's move rule on certain digits."""

    def __init__(self, board: Board, digits: list[int]):
        """Initialize the Knight constraint with the specified board and digits.

        Args:
            board (Board): The Sudoku board on which the constraint applies.
            digits (list[int]): The digits to which the knight's move rule applies.
        """
        super().__init__(board, [])
        self.add_items([Cell.make(board, row, column) for row in board.row_range for column in board.column_range])
        self.digits = digits

    @classmethod
    def parser(cls) -> DigitsParser:
        """Provide the parser for extracting digits for the knight constraint.

        Returns:
            DigitsParser: A parser to extract digits from input.
        """
        return DigitsParser()

    @staticmethod
    def offsets() -> list[Coord]:
        """Define the relative coordinates for knight's moves.

        Returns:
            list[Coord]: list of offsets representing knight's moves.
        """
        return [
            Coord(-1, -2),
            Coord(1, -2),
            Coord(-2, -1),
            Coord(-2, 1),
            Coord(-1, 2),
            Coord(1, 2),
            Coord(2, 1),
            Coord(2, -1)
        ]

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
        return [int(d) for d in yaml[cls.__name__].split(",")]

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start Knight constraint from YAML configuration.

        Args:
            board (Board): The board on which this constraint is created.
            yaml (dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated Knight constraint.
        """
        digits = Knight.extract(board, yaml)
        return Knight(board, digits)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules enforced by this constraint.

        Returns:
            list[Rule]: Rules indicating that each specified digit must be reachable
                        by start knight's move from at least one identical digit.
        """
        return [
            Rule("Knight", 1,
                 f"Every digit in {self.digits!r} must see at least one identical digit via start knights move")
        ]

    def __repr__(self) -> str:
        """Return start string representation of the Knight constraint.

        Returns:
            str: String representation of the constraint.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the knight constraint to the solver.

        Args:
            solver (PulpSolver): The solver to which the constraint is added.
        """
        for digit in self.digits:
            for cell in self.cells:
                include = []
                for offset in Direction.knights():
                    if self.board.is_valid_coordinate(cell.coord + offset):
                        include.append(cell.coord + offset)
                start = solver.choices[digit][cell.row][cell.column]
                possibles = lpSum([solver.choices[digit][i.row][i.column] for i in include])
                solver.model += start <= possibles, f"{self.name}_{cell.row}_{cell.column}_{digit}"

    def to_dict(self) -> dict:
        """Serialize the Knight constraint to start dictionary format.

        Returns:
            dict: Dictionary representation of the constraint.
        """
        return {self.__class__.__name__: ", ".join([str(d) for d in self.digits])}
