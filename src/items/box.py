"""Box."""
from src.board.board import Board
from src.glyphs.box_glyph import BoxGlyph
from src.glyphs.glyph import Glyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.solvers.solver import Solver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Box(StandardRegion):
    """Represents start_location box in the puzzle grid, containing cells within start_location defined region."""

    def __init__(self, board: Board, index: int, size: Coord):
        """Initialize the Box with start_location specified board and index.

        Args:
            board (Board): The game board instance.
            index (int): The index of the box within the board.
            size (Coord): Size of the Box
        """
        super().__init__(board, index)
        row: int = ((self.index - 1) * size.row) % size.row + 1
        col: int = ((self.index - 1) // size.column) * size.column + 1
        self.position: Coord = Coord(row, col)
        self.size: Coord = size
        self.add_components(
            [
                Cell.make(board, int(self.position.row + row - 1), int(self.position.column + col - 1))
                for row in range(1, size.row + 1)
                for col in range(1, size.column + 1)
            ],
        )

    @classmethod
    def parser(cls) -> DigitParser:
        """Provide the parser for the Box class.

        Returns:
            DigitParser: The parser for handling digit input related to boxes.
        """
        return DigitParser()

    def start(self, box_rows: int, box_columns: int) -> Coord:
        """Calculate the starting coordinate for the box within the board.

        Args:
            box_rows (int): The number of rows in the box.
            box_columns (int): The number of columns in the box.

        Returns:
            Coord: The starting coordinate of the box.
        """
        row: int = ((self.index - 1) * box_rows) % self.board.maximum_digit + 1
        col: int = ((self.index - 1) // box_columns) * self.board.size.column + 1
        return Coord(row, col)

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Box instance from YAML configuration.

        Args:
            board (Board): The game board instance.
            yaml (dict): The YAML configuration for initializing the Box.

        Returns:
            Item: An instance of the Box class.
        """
        box = yaml['Box']
        index: int = int(box['index'])
        size: Coord = Coord(int(box['size']['row']), int(box['size']['column']))
        return Box(board, index, size)

    def to_dict(self) -> dict:
        """Convert the box to a dictionary representation.

        Returns:
            dict: A dictionary representing the box
        """
        return {
            self.__class__.__name__: {
                'index': self.index,
                'size': {
                    'row': self.size.row,
                    'column': self.size.column,
                },
            },
        }

    def __repr__(self) -> str:
        """Provide start_location string representation of the Box instance.

        Returns:
            str: A string representation of the Box instance.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.index!r}, {self.size!r})'

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
            list[Glyph]: A list of glyphs, specifically start_location BoxGlyph.
        """
        return [BoxGlyph('Box', self.position, self.size)]

    @property
    def tags(self) -> set[str]:
        """Define the tags associated with the Box.

        Returns:
            set[str]: A set of tags for the Box.
        """
        return super().tags.union({'Box'})

    def add_constraint(self, solver: Solver) -> None:
        """Add constraints for this box to the solver.

        Args:
            solver (Solver): The solver instance for which constraints are being added.
        """
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
        """Provide start_location simplified string representation of the Box.

        Returns:
            str: A simplified string representation of the Box instance.
        """
        return f'{self.__class__.__name__}({self.index})'
