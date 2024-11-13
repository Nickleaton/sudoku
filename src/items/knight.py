from typing import List, Any, Dict

from pulp import lpSum

from src.items.board import Board
from src.items.cell import Cell
from src.items.composed_item import ComposedItem
from src.items.item import Item
from src.parsers.digits_parser import DigitsParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class Knight(ComposedItem):
    """Represents a constraint that enforces a knight's move rule on certain digits."""

    def __init__(self, board: Board, digits: List[int]):
        """
        Initializes the Knight constraint with the specified board and digits.

        Args:
            board (Board): The Sudoku board on which the constraint applies.
            digits (List[int]): The digits to which the knight's move rule applies.
        """
        super().__init__(board, [])
        self.add_items([Cell.make(board, row, column) for row in board.row_range for column in board.column_range])
        self.digits = digits

    @classmethod
    def parser(cls) -> DigitsParser:
        """
        Provides the parser for extracting digits for the knight constraint.

        Returns:
            DigitsParser: A parser to extract digits from input.
        """
        return DigitsParser()

    @staticmethod
    def offsets() -> List[Coord]:
        """
        Defines the relative coordinates for knight's moves.

        Returns:
            List[Coord]: List of offsets representing knight's moves.
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
        """
        Returns tags associated with this constraint.

        Returns:
            set[str]: Tags including 'Knight'.
        """
        return super().tags.union({'Knight'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """
        Extracts digits from YAML configuration.

        Args:
            board (Board): The Sudoku board for context.
            yaml (Dict): The YAML configuration containing digits.

        Returns:
            Any: List of digits extracted from the YAML configuration.
        """
        return [int(d) for d in yaml[cls.__name__].split(",")]

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """
        Factory method to create a Knight constraint from YAML configuration.

        Args:
            board (Board): The board on which this constraint is created.
            yaml (Dict): YAML configuration for the constraint.

        Returns:
            Item: The instantiated Knight constraint.
        """
        digits = Knight.extract(board, yaml)
        return Knight(board, digits)

    @property
    def rules(self) -> List[Rule]:
        """
        Returns the list of rules enforced by this constraint.

        Returns:
            List[Rule]: Rules indicating that each specified digit must be reachable
                        by a knight's move from at least one identical digit.
        """
        return [
            Rule("Knight", 1,
                 f"Every digit in {self.digits!r} must see at least one identical digit via a knights move")
        ]

    def __repr__(self) -> str:
        """
        Returns a string representation of the Knight constraint.

        Returns:
            str: String representation of the constraint.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"

    def add_constraint(self, solver: PulpSolver) -> None:
        """
        Adds the knight constraint to the solver.

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

    def to_dict(self) -> Dict:
        """
        Serializes the Knight constraint to a dictionary format.

        Returns:
            Dict: Dictionary representation of the constraint.
        """
        return {self.__class__.__name__: ", ".join([str(d) for d in self.digits])}
