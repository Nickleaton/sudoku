"""Variables module."""
from enum import IntEnum
from typing import Any, Iterable, Dict

from pulp import LpVariable, LpInteger
from pydotted import pydot

from src.board.board import Board
from src.board.cell_types import ParityType, ModuloType, PrimeType, EntropicType


class Variable(IntEnum):
    """Enumeration of possible variable types."""
    choice = 0
    value = 1
    parity = 2
    entropic = 3
    modulo = 4
    prime = 5


class Variables(pydot):
    """Represents a collection of variables for a board.

    Attributes:
        board (Board): The board associated with the variables.
        variables (Iterable[Variable]): A collection of variables to add to the board.
    """

    def __init__(self, board: Board, variables: Iterable[Variable]):
        """Initializes a Variables instance and adds specified variables.

        Args:
            board (Board): The board to which the variables are associated.
            variables (Iterable[Variable]): The list of variables to initialize.
        """
        super().__init__()
        self.board: Board = board
        self.variables: Iterable[Variable] = variables

        for variable in variables:
            if variable == Variable.choice:
                self.add_choices()
            elif variable == Variable.value:
                self.add_values()
            elif variable == Variable.parity:
                self.add_parity()
            elif variable == Variable.entropic:
                self.add_entropic()
            elif variable == Variable.modulo:
                self.add_modulo()
            elif variable == Variable.prime:
                self.add_prime()

    def add_choices(self) -> None:
        """Adds choice variables to the board."""
        self['choices']: Dict[Any, LpVariable] = LpVariable.dicts(
            name='choices',
            indices=(self.board.digit_range, self.board.row_range, self.board.column_range),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_values(self) -> None:
        """Adds value variables to the board."""

        # It's a dict, so can't use values because its a method, so use values_
        self['values_']: Dict[Any, LpVariable] = LpVariable.dicts(
            name='values_',
            indices=(self.board.row_range, self.board.column_range),
            lowBound=1,
            upBound=self.board.maximum_digit,
            cat=LpInteger,
        )

    def add_parity(self) -> None:
        """Adds parity variables to the board."""
        self['parity']: Dict[Any, LpVariable] = LpVariable.dicts(
            name='parity',
            indices=(self.board.row_range, self.board.column_range, list(ParityType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_entropic(self) -> None:
        """Adds entropic variables to the board."""
        self['entropic']: Dict[Any, LpVariable] = LpVariable.dicts(
            name='entropic',
            indices=(self.board.row_range, self.board.column_range, list(EntropicType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_modulo(self) -> None:
        """Adds modulo variables to the board."""
        self['modulo']: Dict[Any, LpVariable] = LpVariable.dicts(
            name='modulo',
            indices=(self.board.row_range, self.board.column_range, list(ModuloType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )

    def add_prime(self) -> None:
        """Adds prime variables to the board."""
        self['prime']: dict[Any, LpVariable] = LpVariable.dicts(
            name='prime',
            indices=(self.board.row_range, self.board.column_range, list(PrimeType)),
            lowBound=0,
            upBound=1,
            cat=LpInteger,
        )
