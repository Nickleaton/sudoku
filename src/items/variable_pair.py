"""VariablePair."""
import re
from typing import List, Tuple, Dict, Optional

from pulp import LpElement, LpVariable

from src.glyphs.circle_glyph import CircleGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.cell import Cell
from src.items.item import Item
from src.items.pair import Pair
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuException
from src.utils.variable_type import VariableType


class VariablePair(Pair):
    """Represents a pair of cells with an associated variable for a constraint."""

    def __init__(self, board: Board, cell_1: Cell, cell_2: Cell, var_name: str):
        """Initialize a VariablePair instance.

        Args:
            board (Board): The board the pair belongs to.
            cell_1 (Cell): The first cell in the pair.
            cell_2 (Cell): The second cell in the pair.
            var_name (str): The name of the variable associated with the pair.
        """
        super().__init__(board, cell_1, cell_2)
        self.var_name = var_name

    def __repr__(self) -> str:
        """Return a string representation of the VariablePair instance."""
        return f"{self.__class__.__name__}({self.board!r}, {self.cell_1!r}, {self.cell_2!r}, {self.var_name!r})"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Tuple:
        """Extract the coordinates and variable name from the YAML data.

        Args:
            board (Board): The board to extract coordinates for.
            yaml (Dict): The YAML data containing the pair definition.

        Returns:
            Tuple: A tuple containing two Cell objects and the variable name.
        """
        rc_pattern = f"[{board.digit_values}][{board.digit_values}]"
        var_pattern = "[a-zA-Z][a-zA-Z]*"
        regex = re.compile(f"({rc_pattern})-({rc_pattern})=({var_pattern})")
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        c1_str, c2_str, var_str = match.groups()
        c1 = Cell.make(board, int(c1_str[0]), int(c1_str[1]))
        c2 = Cell.make(board, int(c2_str[0]), int(c2_str[1]))
        return c1, c2, var_str

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a VariablePair instance from the YAML data.

        Args:
            board (Board): The board to create the pair on.
            yaml (Dict): The YAML data containing the pair definition.

        Returns:
            Item: A VariablePair instance.
        """
        c1, c2, var_name = cls.extract(board, yaml)
        return cls(board, c1, c2, var_name)

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the VariablePair."""
        return super().tags.union({'Variable Pair'})

    @property
    def label(self) -> str:
        """Get the label associated with the VariablePair."""
        return ""

    def glyphs(self) -> List[Glyph]:
        """Generate glyphs for the VariablePair instance."""
        return [
            CircleGlyph(
                self.__class__.__name__,
                Coord.middle(self.cell_1.coord.center, self.cell_2.coord.center),
                0.15
            )
        ]

    def to_dict(self) -> Dict:
        """Convert the VariablePair to a dictionary representation."""
        return {
            self.__class__.__name__: f"{self.cell_1.row_column_string}-{self.cell_2.row_column_string}={self.var_name}"
        }

    def target(self, solver: PulpSolver) -> Optional[LpElement]:
        """Define the target variable for the pair in the solver.

        Args:
            solver (PulpSolver): The solver to add the target for.

        Returns:
            Optional[LpElement]: The target variable or None if not defined.
        """
        return None

    def variable_type(self) -> VariableType:
        """Return the variable type for the pair.

        Returns:
            VariableType: The type of the variable (integer).
        """
        return VariableType.INT

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
