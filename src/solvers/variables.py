"""Variables module."""
from collections.abc import Iterable
from enum import IntEnum

from pulp import LpInteger  # noqa: I001
from pulp import LpVariable  # noqa: I001

from src.board.board import Board
from src.board.cell_types import EntropicType  # noqa: I001
from src.board.cell_types import ModuloType  # noqa: I001
from src.board.cell_types import ParityType  # noqa: I001
from src.board.cell_types import PrimeType  # noqa: I001
from src.utils.variable_type import VariableType


class VariableSet(IntEnum):
    """Enumeration of possible variable types."""

    choice = 0
    number = 1
    parity = 2
    entropic = 3
    modulo = 4
    prime = 5


class Variables:
    """Represents a collection of variables for a board.

    Attributes:
        board (Board): The board associated with the variables.
        variables (Iterable[VariableSet]): A collection of variables to add to the board.
    """

    def __init__(self, board: Board, variables: Iterable[VariableSet]):
        """Initialize a Variables instance and adds specified variables.

        Args:
            board (Board): The board to which the variables are associated.
            variables (Iterable[VariableSet]): The list of variables to initialize.
        """
        super().__init__()
        self.board: Board = board
        self.odds: dict[str, LpVariable] = {}
        self.choices: dict[tuple[int, int, int], LpVariable] = {}
        self.numbers: dict[tuple[int, int], LpVariable] = {}
        self.parity: dict[tuple[int, int, ParityType], LpVariable] = {}
        self.entropic: dict[tuple[int, int, EntropicType], LpVariable] = {}
        self.modulo: dict[tuple[int, int, ModuloType], LpVariable] = {}
        self.prime: dict[tuple[int, int, PrimeType], LpVariable] = {}

        for variable_type in variables:
            match variable_type:
                case VariableSet.choice:
                    self.add_choices()
                case VariableSet.number:
                    self.add_numbers()
                case VariableSet.parity:
                    self.add_parity()
                case VariableSet.entropic:
                    self.add_entropic()
                case VariableSet.modulo:
                    self.add_modulo()
                case VariableSet.prime:
                    self.add_prime()

    def add_choices(self) -> None:
        """Add choice variables to the board."""
        self.choices = LpVariable.dicts(
            name='choices',
            indices=(self.board.digits.digit_range, self.board.row_range, self.board.column_range),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_numbers(self) -> None:
        """Add number variables to the board."""
        self.numbers = LpVariable.dicts(
            name='numbers',
            indices=(self.board.row_range, self.board.column_range),
            lowBound=1,
            upBound=self.board.digits.maximum,
            cat=LpInteger,
        )

    def add_parity(self) -> None:
        """Add parity variables to the board."""
        self.parity = LpVariable.dicts(
            name='parity',
            indices=(self.board.row_range, self.board.column_range, list(ParityType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_entropic(self) -> None:
        """Add entropic variables to the board."""
        self.entropic = LpVariable.dicts(
            name='entropic',
            indices=(self.board.row_range, self.board.column_range, list(EntropicType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_modulo(self) -> None:
        """Add modulo variables to the board."""
        self.modulo = LpVariable.dicts(
            name='modulo',
            indices=(self.board.row_range, self.board.column_range, list(ModuloType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_prime(self) -> None:
        """Add prime variables to the board."""
        self.prime = LpVariable.dicts(
            name='prime',
            indices=(self.board.row_range, self.board.column_range, list(PrimeType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add(self, name: str, variable_type: VariableType) -> LpVariable:
        """Add a named variable.

        Args:
            name (str): The name of the variable.
            variable_type (VariableType): The type of the variable.

        Returns:
            LpVariable: The created variable.
        """
        if name not in self.odds:
            new_variable: LpVariable = LpVariable(name, cat=variable_type)
            self.odds[name] = new_variable
        return self.odds[name]
