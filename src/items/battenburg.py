"""Battenburg."""
import re
from typing import List, Any, Dict

from src.glyphs.battenburg_glyph import BattenburgGlyph
from src.glyphs.glyph import Glyph
from src.items.board import Board
from src.items.item import Item
from src.parsers.cell_list_parser import CellListParser
from src.solvers.pulp_solver import PulpSolver
from src.utils.coord import Coord
from src.utils.rule import Rule


class Battenburg(Item):
    """Represent a Battenburg pattern in a puzzle.

    The Battenburg pattern is defined by its position on the board,
    constraints for adjacent cells, and methods for parsing, serialization,
    and rendering.

    Attributes:
        position (Coord): The position of the Battenburg pattern on the board.
    """

    def __init__(self, board: Board, position: Coord):
        """Initialize a Battenburg pattern with the given board and position.

        Args:
            board (Board): The puzzle board on which the Battenburg pattern is placed.
            position (Coord): The coordinate position of the Battenburg pattern.
        """
        super().__init__(board)
        self.position = position

    def __repr__(self) -> str:
        """Represent the Battenburg object as a string for debugging.

        Returns:
            str: A string representation of the Battenburg object.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r})"

    @property
    def rules(self) -> List[Rule]:
        """Define the rules associated with the Battenburg pattern.

        Returns:
            List[Rule]: A list containing rules related to the Battenburg pattern.
        """
        return [Rule('Quadruple', 3, 'Digits appearing in at least one of the cells adjacent to the circle')]

    def glyphs(self) -> List[Glyph]:
        """Create glyph representations of the Battenburg pattern for rendering.

        Returns:
            List[Glyph]: A list containing a BattenburgGlyph for graphical representation.
        """
        return [BattenburgGlyph(class_name="Battenburg", coord=self.position)]

    @classmethod
    def parser(cls) -> CellListParser:
        """Provide a parser for interpreting Battenburg configurations.

        Returns:
            CellListParser: A parser for handling cell lists in the Battenburg configuration.
        """
        return CellListParser()

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract the position of the Battenburg pattern from YAML data.

        Args:
            board (Board): The puzzle board, containing board constraints.
            yaml (Dict): The YAML data from which to extract the Battenburg's position.

        Returns:
            Coord: The coordinate position of the Battenburg pattern.

        Raises:
            AssertionError: If the regex pattern does not match the input YAML.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])")
        match = regex.match(str(yaml[cls.__name__]))
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        row_str, column_str = match.groups()
        return Coord(int(row_str), int(column_str))

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a Battenburg item from YAML data.

        Args:
            board (Board): The puzzle board on which the Battenburg will be placed.
            yaml (Dict): The YAML data used to create the Battenburg item.

        Returns:
            Item: An instance of the Battenburg item.
        """
        position = Battenburg.extract(board, yaml)
        return cls(board, position)

    def add_constraint(self, solver: PulpSolver) -> None:
        """Add puzzle constraints for the Battenburg pattern to the solver.

        Args:
            solver (PulpSolver): The solver instance to which the constraints are added.
        """
        _ = (Coord(0, 0), Coord(0, 1), Coord(1, 0), Coord(1, 1))
        # TODO Constraints implementation will go here

    def to_dict(self) -> Dict:
        """Convert the Battenburg item to a dictionary for serialization.

        The dictionary has a single key-value pair where the key is the
        item's class name, and the value is the row and column values of the
        item's position.

        Returns:
            Dict: A dictionary containing the item's class name and position.
        """
        return {self.__class__.__name__: self.position.row * 10 + self.position.column}
