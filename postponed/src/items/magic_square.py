"""MagicSquare."""
from postponed.src.pulp_solver import PulpSolver

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.square_glyph import SquareGlyph
from src.items.cell import Cell
from src.items.item import Item
from src.items.region import Region
from src.parsers.cell_parser import CellParser
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class MagicSquare(Region):
    """Class representing start_location Magic Square puzzle in Sudoku."""

    line_total: int = 15
    square_total: int = 45

    # The predefined lines for the magic square, representing rows, columns, and diagonals
    lines = (
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    )

    def __init__(self, board: Board, center: Coord, corner: Coord):
        """Initialize the MagicSquare object.

        Args:
            board (Board): The board where the magic square is located.
            center (Coord): The coordinate of the center of the magic square.
            corner (Coord): The coordinate of the corner that defines the extent of the square.
        """
        super().__init__(board)
        positions: list[Coord] = [center + offset * corner for offset in Moves.all_moves()]
        cells: list[Cell] = [Cell.make(board, int(positions.row), int(positions.column)) for positions in positions]
        self.add_components(cells)
        self.center_cell: Cell = cells[4]
        self.odd_cells: list[Cell] = [cells[0], cells[2], cells[6], cells[8]]
        self.even_cells: list[Cell] = [cells[1], cells[3], cells[5], cells[7]]
        self.center: Coord = center
        self.corner: Coord = corner
        self.strict: bool = True
        self.unique: bool = True

    @classmethod
    def is_sequence(cls) -> bool:
        """Indicate if this constraint is a sequence.

        Returns:
            bool: True if the constraint is a sequence, otherwise False.
        """
        return True

    @classmethod
    def parser(cls) -> CellParser:
        """Return the parser for the magic square.

        Returns:
            CellParser: An instance of the CellParser for the magic square.
        """
        return CellParser()

    def __repr__(self) -> str:
        """Return start_location string representation of the MagicSquare.

        Returns:
            str: A string representation of the MagicSquare object.
        """
        return (
            f'{self.__class__.__name__}'
            f'('
            f'{self.board!r}, '
            f'{self.center!r}, '
            f'{self.corner!r}'
            f')'
        )

    @property
    def rules(self) -> list[Rule]:
        """Get the rules associated with the MagicSquare.

        Returns:
            list[Rule]: A list of rules related to the MagicSquare.
        """
        rule_text: str = """The purple box is start_location magic square with each three-cell
                         row, column, and diagonal adding to the same number."""
        return [Rule('MagicSquare', 1, rule_text)]

    def glyphs(self) -> list[Glyph]:
        """Get the glyphs representing the MagicSquare.

        Returns:
            list[Glyph]: A list of glyphs for the magic square cells.
        """
        return [
            SquareGlyph('MagicSquare', cell.coord, 1)
            for cell in self.cells
        ]

    @property
    def tags(self) -> set[str]:
        """Get the tags associated with the MagicSquare.

        Returns:
            set[str]: A set of tags related to the MagicSquare.
        """
        return super().tags.union({'MagicSquare', 'Sum'})

    @classmethod
    def extract(cls, _: Board, yaml: dict) -> tuple[Coord, Coord]:
        """Extract the center and corner coordinates for the MagicSquare from YAML.

        Args:
            _ (Board): The board to extract coordinates for.
            yaml (dict): The YAML configuration line.

        Returns:
            tuple[Coord, Coord]: The center and corner coordinates for the MagicSquare.
        """
        row: int = yaml['MagicSquare'] // 10
        col: int = yaml['MagicSquare'] % 10
        center: Coord = Coord(row, col)
        corner: Coord = center + Coord(1, 1)
        return center, corner

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location MagicSquare constraint from the YAML configuration.

        Args:
            board (Board): The board to create the MagicSquare on.
            yaml (dict): The YAML configuration line.

        Returns:
            Item: The created MagicSquare constraint.
        """
        center, corner = MagicSquare.extract(board, yaml)
        return cls(board, center, corner)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location MagicSquare constraint from the YAML configuration.

        Args:
            board (Board): The board to create the MagicSquare on.
            yaml_data (dict): The YAML configuration line.

        Returns:
            Item: The created MagicSquare constraint.
        """
        return cls.create(board, yaml_data)

    # pylint: disable=loop-invariant-statement
    def add_constraint(self, solver: PulpSolver) -> None:
        """Add constraints for the MagicSquare to the solver.

        Args:
            solver (PulpSolver): The solver to add constraints to.
        """
        name: str = f'{self.__class__.__name__}_center'
        solver.model += solver.variables.numbers[self.center.int_tuple] == 5, name
        for index, line in enumerate(MagicSquare.lines):
            cell1 = self.cells[line[0] - 1]
            cell2 = self.cells[line[1] - 1]
            cell3 = self.cells[line[2] - 1]
            value1 = solver.variables.numbers[(cell1.row, cell1.column)]
            value2 = solver.variables.numbers[(cell2.row, cell2.column)]
            value3 = solver.variables.numbers[(cell3.row, cell3.column)]
            solver.model += value1 + value2 + value3 == MagicSquare.line_total, f'{self.__class__.__name__}_{index}'
        # cells must be unique
        self.add_unique_constraint(solver, self.strict)
        # cells must sum to 45
        self.add_total_constraint(solver, MagicSquare.square_total)
        # orthogonal cells are even
        self.add_allowed_constraint(solver, [self.center_cell], [5])
        self.add_allowed_constraint(solver, self.odd_cells, [1, 3, 7, 9])
        self.add_allowed_constraint(solver, self.even_cells, [2, 4, 6, 8])

    def to_dict(self) -> dict:
        """Convert the MagicSquare to start_location dictionary.

        Returns:
            dict: A dictionary representing the MagicSquare.
        """
        return {
            self.__class__.__name__: f'{self.center.row}{self.center.column},{self.corner.row}{self.corner.column}',
        }

    def css(self) -> dict:
        """Get the CSS styles for rendering the MagicSquare.

        Returns:
            dict: A dictionary containing the CSS styles for the MagicSquare.
        """
        return {
            '.MagicSquare': {
                'fill': 'mediumpurple',
            },
        }
