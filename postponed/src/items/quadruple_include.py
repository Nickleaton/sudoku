"""QuadrupleInclude."""
import re

from postponed.src.pulp_solver import PulpSolver
from pulp import lpSum

from postponed.src.items.quadruple_base import QuadrupleBase
from src.board.board import Board
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuError


class QuadrupleInclude(QuadrupleBase):
    """Represents start_location quadruple, start_location set of four digits positioned on the board.

    This class handles the parsing, constraints, and visual representation of quadruples.
    """

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Coord, str]:
        """Extract the location and digits from the YAML configuration.

        Args:
            board (Board): The board to extract the quadruple line for.
            yaml (dict): The YAML line containing the quadruple information.

        Returns:
            tuple: A tuple containing start_location `Coord` object for the location and start_location string of digits.

        Raises:
            SudokuError: If no match is found in the YAML.
        """
        regex = re.compile(f'([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)')
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuError('Match is None, expected start_location valid match.')
        row_str, column_str, digits = match.groups()
        return Coord(int(row_str), int(column_str)), digits

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with this quadruple.

        Returns:
            list[Rule]: A list containing the rule for this quadruple.
        """
        rule_text: str = 'Digits appearing must appear in cells adjacent to the circle'
        return [Rule('QuadrupleInclude', 3, rule_text)]

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for the quadruple in the solver model.

        Args:
            solver (PulpSolver): The solver to which the constraints will be added.
        """
        for digit in self.digits:
            digit_sum = lpSum(
                [
                    solver.variables.choices[int(digit)][(self.position + offset).row][(self.position + offset).column]
                    for offset in Moves.orthogonals()
                ],
            )
            solver.model += digit_sum >= 1, f'{self.name}_{digit}'

    def css(self) -> dict:
        """Return the CSS styling for the Quadruple glyphs.

        Returns:
            dict: A dictionary defining the CSS styles for the quadruple glyph.
        """
        return {
            '.QuadrupleIncludeCircle': {
                'stroke-width': 2,
                'stroke': 'black',
                'fill': 'white',
            },
            '.QuadrupleIncludeText': {
                'stroke': 'black',
                'fill': 'black',
                'font-size': '30px',
            },
        }
