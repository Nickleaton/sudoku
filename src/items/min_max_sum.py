import re
from typing import List, Any, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.board import Board
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side


class MinMaxSum(FirstN):
    """
    Handle frame sudoku:
    Numbers outside the frame equal the sum of the minimum and maximum values in the first three cells
    corresponding row or column in the given direction.
    """

    def __init__(self, board: Board, side: Side, index: int, total: int):
        """
        Initialize a MinMaxSum frame.

        Args:
            board (Board): The board where the frame is located.
            side (Side): The side where the total is to go.
            index (int): The row or column of the total.
            total (int): The total sum of the minimum and maximum values.
        """
        super().__init__(board, side, index)
        self.total = total

    def __repr__(self) -> str:
        """
        Return a string representation of the MinMaxSum frame.

        Returns:
            str: A string representation of the object.
        """
        return (
            f"{self.__class__.__name__}("
            f"{self.board!r}, "
            f"{self.side!r}, "
            f"{self.total}"
            f")"
        )

    @property
    def rules(self) -> List[Rule]:
        """
        Get the rules associated with the MinMaxSum frame.

        Returns:
            List[Rule]: A list containing the rules.
        """
        return [
            Rule(
                'MinMaxSum',
                1,
                "Numbers outside the frame equal the sum of the minimum and maximum number in the "
                "corresponding row or column in the given direction"
            )
        ]

    def glyphs(self) -> List[Glyph]:
        """
        Get the glyphs representing the MinMaxSum frame.

        Returns:
            List[Glyph]: A list containing the glyphs for this frame.
        """
        return [
            TextGlyph(
                'MinMaxSumText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.total)
            )
        ]

    @property
    def tags(self) -> set[str]:
        """
        Get the tags associated with the MinMaxSum frame.

        Returns:
            set[str]: A set containing the tags.
        """
        return super().tags.union({'Comparison', 'MinMaxSum', 'Minimum', 'Maximum'})

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """
        Extract the side, index, and total from the YAML configuration.

        Args:
            board (Board): The board the configuration is for.
            yaml (Dict): The YAML configuration data.

        Returns:
            Tuple: A tuple containing the side, index, and total.
        """
        regexp = re.compile(f"([{Side.values()}])([{board.digit_values}])=([0-9]+)")
        match = regexp.match(yaml[cls.__name__])
        assert match is not None
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """
        Create a MinMaxSum frame from the YAML configuration.

        Args:
            board (Board): The board to create the frame on.
            yaml (Dict): The YAML configuration data.

        Returns:
            Item: The created MinMaxSum item.
        """
        side, index, total = MinMaxSum.extract(board, yaml)
        return cls(board, side, index, total)

    def add_constraint(self, solver: PulpSolver) -> None:
        """
        Add the constraint for the MinMaxSum frame to the solver.

        Args:
            solver (PulpSolver): The solver to add the constraint to.
        """
        xi = [solver.values[cell.row][cell.column] for cell in self.cells]
        mini = Formulations.minimum(solver.model, xi, 1, self.board.maximum_digit)
        maxi = Formulations.maximum(solver.model, xi, 1, self.board.maximum_digit)
        solver.model += mini + maxi == self.total, self.name

    def to_dict(self) -> Dict:
        """
        Convert the MinMaxSum frame to a dictionary representation.

        Returns:
            Dict: The dictionary representation of the object.
        """
        return {self.__class__.__name__: f"{self.side.value}{self.index}={self.total}"}

    def css(self) -> Dict:
        """
        Get the CSS styles for rendering the MinMaxSum frame.

        Returns:
            Dict: The dictionary containing CSS styles.
        """
        return {
            ".MinMaxSumTextForeground": {
                "fill": "black",
                "font-size": "30px",
                "stroke": "black",
                "stroke-width": 1
            },
            ".MinMaxSumTextBackground": {
                "fill": "white",
                "font-size": "30px",
                "font-weight": "bolder",
                "stroke": "white",
                "stroke-width": 8
            }
        }
