import re
from typing import List, Any, Dict

from pulp import lpSum

from src.items.board import Board
from src.items.quadruple_base import QuadrupleBase
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class QuadrupleExclude(QuadrupleBase):
    """Represents a quadruple, a set of four digits positioned on the board.

    This class handles the parsing, constraints, and visual representation of quadruples.
    """

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extracts the position and digits from the YAML configuration.

        Args:
            board (Board): The board to extract the quadruple data for.
            yaml (Dict): The YAML data containing the quadruple information.

        Returns:
            tuple: A tuple containing a `Coord` object for the position and a string of digits.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        assert match is not None
        row_str, column_str, digits = match.groups()
        return Coord(int(row_str), int(column_str)), digits

    @property
    def rules(self) -> List[Rule]:
        """Returns the list of rules associated with this quadruple.

        Returns:
            List[Rule]: A list containing the rule for this quadruple.
        """
        return [Rule('QuadrupleExclude', 3, 'Digits appearing must not in the cells adjacent to the circle')]

    def add_constraint(self, solver: PulpSolver) -> None:
        """Adds constraints for the quadruple in the solver model.

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
            solver.model += digit_sum == 0, f"{self.name}_{digit}"

    def css(self) -> Dict:
        """Returns the CSS styling for the Quadruple glyphs.

        Returns:
            Dict: A dictionary defining the CSS styles for the quadruple glyph.
        """
        return {
            ".QuadrupleExcludeCircle": {
                "stroke-width": 2,
                "stroke": "black",
                "fill": "lightpink"
            },
            ".QuadrupleExcludeText": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
