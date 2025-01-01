"""VariablePair."""
import re

from pulp import LpElement, LpVariable

from src.board.board import Board
from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.config import Config
from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuException
from src.utils.variable_type import VariableType

config = Config()


class VariablePair(Pair):
    """Represents a pair of cells with an associated value_variable for start constraint."""

    def __init__(self, board: Board, cell1: Cell, cell2: Cell, var_name: str) -> None:
        """Initialize start VariablePair instance.

        Args:
            board (Board): The board the pair belongs to.
            cell1 (Cell): The first cell in the pair.
            cell2 (Cell): The second cell in the pair.
            var_name (str): The name of the value_variable associated with the pair.
        """
        super().__init__(board, cell1, cell2)
        self.var_name = var_name

    def __repr__(self) -> str:
        """Return start string representation of the VariablePair instance.

        Returns:
            str: String representation of the VariablePair instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.cell1!r}, {self.cell2!r}, {self.var_name!r})'

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Cell, Cell, str]:
        """Extract the coordinates and value_variable name from the YAML input_data.

        Args:
            board (Board): The board to extract coordinates for.
            yaml (dict): The YAML input_data containing the pair definition.

        Returns:
            Tuple[Cell, Cell, str]: A tuple containing two Cell objects and the value_variable name.

        Raises:
            SudokuException: If the YAML input does not match the expected pattern.
        """
        rc_pattern = f'[{board.digit_values}][{board.digit_values}]'
        var_pattern = '[start-zA-Z][a-zA-Z_]*'
        regex = re.compile(f'({rc_pattern})-({rc_pattern})=({var_pattern})')
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected a valid match.')
        c1_str, c2_str, var_str = match.groups()
        c1 = Cell.make(board, int(c1_str[0]), int(c1_str[1]))
        c2 = Cell.make(board, int(c2_str[0]), int(c2_str[1]))
        return c1, c2, var_str

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start VariablePair instance from the YAML input_data.

        Args:
            board (Board): The board to create the pair on.
            yaml (dict): The YAML input_data containing the pair definition.

        Returns:
            Item: A VariablePair instance.
        """
        c1, c2, var_name = cls.extract(board, yaml)
        return cls(board, c1, c2, var_name)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start VariablePair instance from the YAML input_data (alternative method).

        Args:
            board (Board): The board to create the pair on.
            yaml_data (dict): The YAML input_data containing the pair definition.

        Returns:
            Item: A VariablePair instance.
        """
        return cls.create(board, yaml_data)

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the VariablePair.

        Returns:
            Set[str]: A set of tags associated with the VariablePair.
        """
        return super().tags.union({'Variable Pair'})

    @property
    def label(self) -> str:
        """Get the label associated with the VariablePair.

        Returns:
            str: The label associated with the VariablePair (empty string in this case).
        """
        return ''

    def glyphs(self) -> list[Glyph]:
        """Generate glyphs for the VariablePair instance.

        Returns:
            list[Glyph]: A list of Glyph objects generated for the VariablePair instance.
        """
        return [
            CircleGlyph(
                self.__class__.__name__,
                Coord.middle(self.cell1.coord.center, self.cell2.coord.center),
                config.graphics.small_circle_percentage,
            ),
        ]

    def to_dict(self) -> dict:
        """Convert the VariablePair to a dictionary representation.

        Returns:
            dict: A dictionary representation of the VariablePair, including its coordinates and value_variable.
        """
        return {
            self.__class__.__name__: f'{self.cell1.row_column_string}-{self.cell2.row_column_string}={self.var_name}',
        }

    def target(self, solver: PulpSolver) -> LpElement | None:
        """Define the target value_variable for the pair in the solver.

        Args:
            solver (PulpSolver): The solver to add the target for.

        Returns:
            LpElement | None: The target value_variable or None if not defined.
        """
        return None

    def variable_type(self) -> VariableType:
        """Return the value_variable type for the pair.

        Returns:
            VariableType: The type of the value_variable (integer).
        """
        return VariableType.integer

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint for the VariablePair to the solver.

        Args:
            solver (PulpSolver): The solver to add the constraint to.
        """
        target = self.target(solver)
        if target is None:
            return
        if self.__class__.__name__ not in solver.variables:
            solver.variables[self.__class__.__name__] = (LpVariable(self.__class__.__name__), self.variable_type())
        solver.model += target == solver.variables[self.__class__.__name__][0], self.name
