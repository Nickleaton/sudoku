"""QuadrupleInclude."""
import re
from typing import Any

from pulp import lpSum

from src.items.board import Board
from src.items.quadruple_base import QuadrupleBase
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuException


class QuadrupleInclude(QuadrupleBase):
    """Represents a quadruple, a set of four digits positioned on the board.

    This class handles the parsing, constraints, and visual representation of quadruples.
    """

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Any:
        """Extract the position and digits from the YAML configuration.

        Args:
            board (Board): The board to extract the quadruple data for.
            yaml (dict): The YAML data containing the quadruple information.

        Returns:
            tuple: A tuple containing a `Coord` object for the position and a string of digits.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        row_str, column_str, digits = match.groups()
        return Coord(int(row_str), int(column_str)), digits

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with this quadruple.

        Returns:
            list[Rule]: A list containing the rule for this quadruple.
        """
        return [Rule('QuadrupleInclude', 3, 'Digits appearing must appear in cells adjacent to the circle')]

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for the quadruple in the solver model.

        Args:
            solver (PulpSolver): The solver to which the constraints will be added.
        """
        offsets = (
            Coord(0, 0),
            Coord(0, 1),
            Coord(1, 0),
            Coord(1, 1)
        )
        for digit in self.digits:
            digit_sum = lpSum(
                [
                    solver.choices[int(digit)][(self.position + offset).row][(self.position + offset).column]
                    for offset in offsets
                ]
            )
            solver.model += digit_sum >= 1, f"{self.name}_{digit}"

    def css(self) -> dict:
        """Return the CSS styling for the Quadruple glyphs.

        Returns:
            dict: A dictionary defining the CSS styles for the quadruple glyph.
        """
        return {
            ".QuadrupleIncludeCircle": {
                "stroke-width": 2,
                "stroke": "black",
                "fill": "white"
            },
            ".QuadrupleIncludeText": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
