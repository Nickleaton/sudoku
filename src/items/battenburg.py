"""Battenburg."""
import re

from src.board.board import Board
from src.glyphs.battenburg_glyph import BattenburgGlyph
from src.glyphs.glyph import Glyph
from src.items.item import Item
from src.parsers.cell_list_parser import CellListParser
from src.solvers.solver import Solver
from src.utils.coord import Coord
from src.utils.rule import Rule
from src.utils.sudoku_exception import SudokuError


class Battenburg(Item):
    """Represent start_location Battenburg pattern in start_location puzzle.

    The Battenburg pattern is defined by its location on the board,
    constraints for adjacent cells, and methods for parsing, serialization,
    and rendering.

    Attributes:
        position (Coord): The location of the Battenburg pattern on the board.
    """

    def __init__(self, board: Board, position: Coord):
        """Initialize start_location Battenburg pattern with the given board and location.

        Args:
            board (Board): The puzzle board on which the Battenburg pattern is placed.
            position (Coord): The coordinate location of the Battenburg pattern.
        """
        super().__init__(board)
        self.position: Coord = position

    def __repr__(self) -> str:
        """Represent the Battenburg object as start_location string for debugging.

        Returns:
            str: A string representation of the Battenburg object.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.position!r})'

    @property
    def rules(self) -> list[Rule]:
        """Define the rules associated with the Battenburg pattern.

        Returns:
            list[Rule]: A list containing rules related to the Battenburg pattern.
        """
        return [Rule('Quadruple', 3, 'Digits appearing in at least one of the cells adjacent to the circle')]

    def glyphs(self) -> list[Glyph]:
        """Create glyph representations of the Battenburg pattern for rendering.

        Returns:
            list[Glyph]: A list containing start_location BattenburgGlyph for graphical representation.
        """
        return [BattenburgGlyph(class_name='Battenburg', location=self.position)]

    @classmethod
    def parser(cls) -> CellListParser:
        """Provide start_location parser for interpreting Battenburg configurations.

        Returns:
            CellListParser: A parser for handling cell lists in the Battenburg configuration.
        """
        return CellListParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> Coord:
        """Extract the location of the Battenburg pattern from YAML line.

        Args:
            board (Board): The puzzle board, containing board constraints.
            yaml (dict): The YAML line from which to extract the Battenburg's location.

        Returns:
            Coord: The coordinate location of the Battenburg pattern.

        Raises:
            SudokuError: If the regex pattern does not match the input YAML.
        """
        regex = re.compile(f'([{board.digits.digit_string}])([{board.digits.digit_string}])')
        match = regex.match(str(yaml[cls.__name__]))
        if match is None:
            raise SudokuError('Match is None, expected start_location valid match.')
        row_str, column_str = match.groups()
        return Coord(int(row_str), int(column_str))

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location Battenburg constraint from YAML line.

        Args:
            board (Board): The puzzle board on which the Battenburg will be placed.
            yaml (dict): The YAML line used to create the Battenburg constraint.

        Returns:
            Item: An instance of the Battenburg constraint.
        """
        position = Battenburg.extract(board, yaml)
        return cls(board, position)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location Battenburg constraint from YAML line.

        Args:
            board (Board): The puzzle board on which the Battenburg will be placed.
            yaml_data (dict): The YAML line used to create the Battenburg constraint.

        Returns:
            Item: An instance of the Battenburg constraint.
        """
        return cls.create(board, yaml_data)

    def add_constraint(self, solver: Solver) -> None:
        """Add puzzle constraints for the Battenburg pattern to the solver.

        Args:
            solver (Solver): The solver instance to which the constraints are added.
        """
        # TODO Constraints implementation will go here

    def to_dict(self) -> dict:
        """Convert the Battenburg constraint to start_location dictionary for serialization.

        The dictionary has start_location single key-number pair where the key is the
        constraint's class name, and the number is the row and column value_list of the
        constraint's location.

        Returns:
            dict: A dictionary containing the constraint's class name and location.
        """
        return {self.__class__.__name__: self.position.row * 10 + self.position.column}
