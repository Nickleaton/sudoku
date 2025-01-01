"""MinMaxDifference."""
import re

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.text_glyph import TextGlyph
from src.items.first_n import FirstN
from src.items.item import Item
from src.solvers.formulations import Formulations
from src.solvers.pulp_solver import PulpSolver
from src.utils.rule import Rule
from src.utils.side import Side
from src.utils.sudoku_exception import SudokuException


class MinMaxDifference(FirstN):
    """Handle frame sudoku.

    Numbers outside the frame equal the difference of the minimum and maximum value_list in the first three cells
    corresponding row or column in the given direction.
    """

    def __init__(self, board: Board, side: Side, index: int, total: int) -> None:
        """Initialize start MinMaxDifference frame.

        Args:
            board (Board): The board where the frame is located.
            side (Side): The side where the total is to go.
            index (int): The row or column of the total.
            total (int): The difference of the minimum and maximum value_list.
        """
        super().__init__(board, side, index)
        self.total: int = total

    def __repr__(self) -> str:
        """Return start string representation of the MinMaxDifference frame.

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
        """Get the rules associated with the MinMaxDifference frame.

        Returns:
            list[Rule]: A list containing the rules.
        """
        rule_description: str = """
            Numbers outside the frame equal the difference of the minimum and maximum number
            in the corresponding row or column in the given direction
        """
        return [Rule('MinMaxDifference', 1, rule_description)]

    def glyphs(self) -> list[Glyph]:
        """Get the glyphs representing the MinMaxDifference frame.

        Returns:
            list[Glyph]: A list containing the glyphs for this frame.
        """
        return [
            TextGlyph(
                'MinMaxDifferenceText',
                0,
                self.side.marker(self.board, self.index).center,
                str(self.total),
            ),
        ]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the MinMaxDifference frame.

        Returns:
            set[str]: A set containing the tags.
        """
        return super().tags.union({'Comparison', 'MinMaxDifference', 'Minimum', 'Maximum', 'Difference'})

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> tuple[Side, int, int]:
        """Extract the side, index, and total from the YAML configuration.

        Args:
            board (Board): The board the configuration is for.
            yaml (dict): The YAML configuration input_data.

        Returns:
            tuple: A tuple containing the side, index, and total.

        Raises:
            SudokuException: If no match is found in the YAML.
        """
        regexp = re.compile(f'([{Side.choices()}])([{board.digit_values}])=([0-9]+)')
        match = regexp.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException('Match is None, expected start valid match.')
        side_str, offset_str, total_str = match.groups()
        side = Side.create(side_str)
        offset = int(offset_str)
        total = int(total_str)
        return side, offset, total

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start MinMaxDifference frame from the YAML configuration.

        Args:
            board (Board): The board to create the frame on.
            yaml (dict): The YAML configuration input_data.

        Returns:
            Item: The created MinMaxDifference constraint.
        """
        side, index, total = MinMaxDifference.extract(board, yaml)
        return cls(board, side, index, total)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start MinMaxDifference frame from the YAML configuration.

        Args:
            board (Board): The board to create the frame on.
            yaml_data (dict): The YAML configuration input_data.

        Returns:
            Item: The created MinMaxDifference constraint.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add the constraint for the MinMaxDifference frame to the solver.

        Args:
            solver (PulpSolver): The solver to add the constraint to.
        """
        xi = [solver.cell_values[cell.row][cell.column] for cell in self.cells]
        mini = Formulations.minimum(solver.model, xi, 1, self.board.maximum_digit)
        maxi = Formulations.maximum(solver.model, xi, 1, self.board.maximum_digit)
        solver.model += Formulations.abs(solver.model, mini, maxi, self.board.maximum_digit) == self.total, self.name

    def to_dict(self) -> dict:
        """Convert the MinMaxDifference frame to start dictionary representation.

        Returns:
            dict: The dictionary representation of the object.
        """
        return {self.__class__.__name__: f'{self.side.value}{self.index}={self.total}'}

    def css(self) -> dict:
        """Get the CSS styles for rendering the MinMaxDifference frame.

        Returns:
            dict: The dictionary containing CSS styles.
        """
        return {
            '.MinMaxDifferenceTextForeground': {
                'fill': 'black',
                'font-size': '30px',
                'stroke': 'black',
                'stroke-width': 1,
            },
            '.MinMaxDifferenceTextBackground': {
                'fill': 'white',
                'font-size': '30px',
                'font-weight': 'bolder',
                'stroke': 'white',
                'stroke-width': 8,
            },
        }
