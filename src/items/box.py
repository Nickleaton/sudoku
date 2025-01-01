"""Box."""
from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.rect_glyph import BoxGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Box(StandardRegion):
    """Represents start box in the puzzle grid, containing cells within start defined region."""

    def __init__(self, board: Board, index: int):
        """Initialize the Box with start specified board and index.

        Args:
            board (Board): The game board instance.
            index (int): The index of the box within the board.
        """
        super().__init__(board, index)
        self.position = self.start()
        self.add_components(
            [
                Cell.make(board, int(self.position.row + ro - 1), int(self.position.column + co - 1))
                for ro in range(1, board.box_rows + 1)
                for co in range(1, board.box_columns + 1)
            ],
        )

    @classmethod
    def parser(cls) -> DigitParser:
        """Provide the parser for the Box class.

        Returns:
            DigitParser: The parser for handling digit input related to boxes.
        """
        return DigitParser()

    def start(self) -> Coord:
        """Calculate the starting coordinate for the box within the board.

        Returns:
            Coord: The starting coordinate of the box.
        """
        row: int = ((self.index - 1) * self.board.box_rows) % self.board.maximum_digit + 1
        col: int = ((self.index - 1) // self.board.box_columns) * self.board.box_columns + 1
        return Coord(row, col)

    @property
    def size(self) -> Coord:
        """Define the size of the box in terms of rows and columns.

        Returns:
            Coord: The dimensions of the box.
        """
        return Coord(self.board.box_rows, self.board.box_columns)

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start Box instance from YAML configuration.

        Args:
            board (Board): The game board instance.
            yaml (dict): The YAML configuration for initializing the Box.

        Returns:
            Item: An instance of the Box class.
        """
        index = cls.extract(board, yaml)
        return cls(board, index)

    def __repr__(self) -> str:
        """Provide start string representation of the Box instance.

        Returns:
            str: A string representation of the Box instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.index!r})'

    @property
    def rules(self) -> list[Rule]:
        """Define the rules associated with the Box.

        Returns:
            list[Rule]: A list of rules indicating that digits in the box must be unique.
        """
        return [Rule('Box', 1, 'Digits in each box must be unique')]

    def glyphs(self) -> list[Glyph]:
        """Generate glyphs for visual representation of the box.

        Returns:
            list[Glyph]: A list of glyphs, specifically start BoxGlyph.
        """
        return [BoxGlyph('Box', self.position, self.size)]

    @property
    def tags(self) -> set[str]:
        """Define the tags associated with the Box.

        Returns:
            set[str]: A set of tags for the Box.
        """
        return super().tags.union({'Box'})

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for this box to the solver.

        Args:
            solver (PulpSolver): The solver instance for which constraints are being added.
        """
        self.add_total_constraint(solver, solver.board.digit_sum)
        self.add_unique_constraint(solver)

    def css(self) -> dict:
        """Return the CSS styling for the box.

        Returns:
            dict: A dictionary containing CSS properties for the box.
        """
        return {
            '.Box': {
                'stroke': 'black',
                'stroke-width': 3,
                'fill-opacity': 0,
            },
        }

    def __str__(self) -> str:
        """Provide start simplified string representation of the Box.

        Returns:
            str: A simplified string representation of the Box instance.
        """
        return f'{self.__class__.__name__}({self.index})'
