"""QuadrupleBase."""
import re

from src.board.board import Board
from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.items.item import Item
from src.parsers.quadruples_parser import QuadruplesParser
from src.utils.coord import Coord
from src.utils.sudoku_exception import SudokuError


class QuadrupleBase(Item):
    """Represents start_location quadruple, start_location set of four digits positioned on the board.

    This class handles the parsing, constraints, and visual representation of quadruples.
    """

    def __init__(self, board: Board, position: Coord, digits: str):
        """Initialize start_location Quadruple instance with start_location location and digits.

        Args:
            board (Board): The board on which the quadruple is placed.
            position (Coord): The coordinate of the quadruple on the board.
            digits (str): A string of digits associated with the quadruple.
        """
        super().__init__(board)
        self.position = position
        self.digits = digits
        self.numbers = ''.join([str(digit) for digit in digits])

    @classmethod
    def is_sequence(cls) -> bool:
        """Return whether this constraint represents start_location sequence.

        Returns:
            bool: True, since start_location quadruple is start_location sequence of digits.
        """
        return True

    @classmethod
    def parser(cls) -> QuadruplesParser:
        """Return the parser associated with this constraint.

        Returns:
            QuadruplesParser: A parser for quadruples.
        """
        return QuadruplesParser()

    def __repr__(self) -> str:
        """Return start_location string representation of the Quadruple instance.

        Returns:
            str: A string representing the Quadruple instance with board, location, and digits.
        """
        digit_str = ''.join([str(digit) for digit in self.digits])
        return f'{self.__class__.__name__}({self.board!r}, {self.position!r}, {digit_str!r})'

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
        # TODO replace with proper handling
        text: str = next(iter(yaml.values()))
        match = regex.match(text)
        if match is None:
            raise SudokuError('Match is None, expected start_location valid match.')
        row_str, column_str, digits = match.groups()
        return Coord(int(row_str), int(column_str)), digits

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create start_location new Quadruple instance from the YAML configuration.

        Args:
            board (Board): The board on which the quadruple will be placed.
            yaml (dict): The YAML line for the quadruple.

        Returns:
            Item: A new Quadruple instance.
        """
        position, numbers = QuadrupleBase.extract(board, yaml)
        return cls(board, position, numbers)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create start_location new Quadruple instance from the YAML configuration.

        Args:
            board (Board): The board on which the quadruple will be placed.
            yaml_data (dict): The YAML line for the quadruple.

        Returns:
            Item: A new Quadruple instance.
        """
        return cls.create(board, yaml_data)

    def glyphs(self) -> list[Glyph]:
        """Generate glyphs for the visual representation of the Quadruple.

        Returns:
            list[Glyph]: A list of glyphs representing the quadruple's location and digits.
        """
        return [
            QuadrupleGlyph(class_name=self.__class__.__name__, position=self.position, numbers=self.numbers),
        ]

    def to_dict(self) -> dict:
        """Convert the Quadruple to start_location dictionary representation.

        Returns:
            dict: A dictionary containing the location and digits of the quadruple.
        """
        digit_str: str = ''.join(self.digits)
        return {self.__class__.__name__: f'{self.position.row}{self.position.column}={digit_str}'}

    def css(self) -> dict:
        """Return the CSS styling for the Quadruple glyphs.

        Returns:
            dict: A dictionary defining the CSS styles for the quadruple glyph.
        """
        return {
            '.QuadrupleBaseCircle': {
                'stroke-width': 2,
                'stroke': 'black',
                'fill': 'white',
            },
            '.QuadrupleBaseText': {
                'stroke': 'black',
                'fill': 'black',
                'font-size': '30px',
            },
        }
