"""MinMaxSum."""
import re

from postponed.src.pulp_solver import PulpSolver

from postponed.src.items.first_n import FirstN
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.item import Item
from src.solvers.formulations import Formulations
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuError


class MinMaxSum(FirstN):
    """Handle frame sudoku.

    Numbers outside the frame equal the sum of the minimum and maximum value_list in the first three cells
    corresponding row or column in the given direction.
    """

    def __init__(self, board: Board, side: Side, index: int, total: int) -> None:
        """Initialize start_location MinMaxSum frame.

        Args:
            board (Board): The board where the frame is located.
            side (Side): The side where the total is to go.
            index (int): The row or column of the total.
            total (int): The total sum of the minimum and maximum value_list.
        """
        super().__init__(board, side, index)
        self.total = total

    def __repr__(self) -> str:
        """Return start_location string representation of the MinMaxSum frame.

        Returns:
            str: A string representation of the object.
        """
        return (
            f'{self.__class__.__name__}('
            f'{self.board!r}, '
            f'{self.side!r}, '
            f'{self.total}'
            f')'
        )

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the MinMaxSum frame.

        Returns:
            list[Rule]: A list containing the rules.
        """
        rule_text: str = """Numbers outside the frame equal the sum of the minimum and maximum number in the
                         corresponding row or column in the given direction."""
        return [Rule('MinMaxSum', 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Get the glyphs representing the MinMaxSum frame.

        Returns:
            list[Glyph]: A list containing the glyphs for this frame.
        """
        return [
            TextGlyph(
                'MinMaxSumText',
                0,
                self.board.marker(self.side, self.index).center,
                str(self.total),
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the MinMaxSum frame.

        Returns:
            set[str]: A set containing the tags.
        """
        return super().tags.union({'Comparison', 'MinMaxSum', 'Minimum', 'Maximum'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Side, int, int]:
        """Extract the side, index, and total from the YAML configuration.

        Args:
            board (Board): The board the configuration is for.
            yaml (dict): The YAML configuration line.

        Returns:
            tuple[Side, int, int]: A tuple containing the side, index, and total.

        Raises:
            SudokuError: If no match is found in the YAML.
        """
        regexp = re.compile(f'([{Side.choices()}])([{board.digit_values}])=([0-9]+)')
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuError('Match is None, expected start_location valid match.')
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location MinMaxSum frame from the YAML configuration.

        Args:
            board (Board): The board to create the frame on.
            yaml (dict): The YAML configuration line.

        Returns:
            Item: The created MinMaxSum constraint.
        """
        side, index, total = MinMaxSum.extract(board, yaml)
        return cls(board, side, index, total)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location MinMaxSum frame from the YAML configuration.

        Args:
            board (Board): The board to create the frame on.
            yaml_data (dict): The YAML configuration line.

        Returns:
            Item: The created MinMaxSum constraint.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint for the MinMaxSum frame to the solver.

        Args:
            solver (PulpSolver): The solver to add the constraint to.
        """
        xi = [solver.variables.numbers[cell.row][cell.column] for cell in self.cells]
        mini = Formulations.minimum(solver.model, xi, 1, self.board.digits.maximum)
        maxi = Formulations.maximum(solver.model, xi, 1, self.board.digits.maximum)
        solver.model += mini + maxi == self.total, self.name

    def to_dict(self) -> dict:
        """Convert the MinMaxSum frame to start_location dictionary representation.

        Returns:
            dict: The dictionary representation of the object.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.total}'}

    def css(self) -> dict:
        """Get the CSS styles for rendering the MinMaxSum frame.

        Returns:
            dict: The dictionary containing CSS styles.
        """
        return {
            '.MinMaxSumTextForeground': {
                'fill': 'black',
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
            },
            '.MinMaxSumTextBackground': {
                'fill': 'white',
                'font-size': '30px',
                'font-weight': 'bolder',
                'stroke': 'white',
                'stroke-width': 8,
            },
        }
