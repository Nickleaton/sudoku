"""QuadrupleBase."""
import re
from typing import List, Any, Dict

from src.glyphs.glyph import Glyph
from src.glyphs.quadruple_glyph import QuadrupleGlyph
from src.items.board import Board
from src.items.item import Item
from src.parsers.quadruples_parser import QuadruplesParser
from src.utils.coord import Coord


class QuadrupleBase(Item):
    """Represents a quadruple, a set of four digits positioned on the board.

    This class handles the parsing, constraints, and visual representation of quadruples.
    """

    def __init__(self, board: Board, position: Coord, digits: str):
        """Initialize a Quadruple instance with a position and digits.

        Args:
            board (Board): The board on which the quadruple is placed.
            position (Coord): The coordinate of the quadruple on the board.
            digits (str): A string of digits associated with the quadruple.
        """
        super().__init__(board)
        self.position = position
        self.digits = digits
        self.numbers = "".join([str(d) for d in digits])

    @classmethod
    def is_sequence(cls) -> bool:
        """Return whether this item represents a sequence.

        Returns:
            bool: True, since a quadruple is a sequence of digits.
        """
        return True

    @classmethod
    def parser(cls) -> QuadruplesParser:
        """Return the parser associated with this item.

        Returns:
            QuadruplesParser: A parser for quadruples.
        """
        return QuadruplesParser()

    def __repr__(self) -> str:
        """Return a string representation of the Quadruple instance.

        Returns:
            str: A string representing the Quadruple instance with board, position, and digits.
        """
        digit_str = "".join([str(digit) for digit in self.digits])
        return f"{self.__class__.__name__}({self.board!r}, {self.position!r}, '{digit_str}')"

    @classmethod
    def extract(cls, board: Board, yaml: Dict) -> Any:
        """Extract the position and digits from the YAML configuration.

        Args:
            board (Board): The board to extract the quadruple data for.
            yaml (Dict): The YAML data containing the quadruple information.

        Returns:
            tuple: A tuple containing a `Coord` object for the position and a string of digits.
        """
        regex = re.compile(f"([{board.digit_values}])([{board.digit_values}])=([{board.digit_values}]+)")
        match = regex.match(yaml[cls.__name__])
        if match is None:
            raise SudokuException("Match is None, expected a valid match.")
        row_str, column_str, digits = match.groups()
        return Coord(int(row_str), int(column_str)), digits

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create a new Quadruple instance from the YAML configuration.

        Args:
            board (Board): The board on which the quadruple will be placed.
            yaml (Dict): The YAML data for the quadruple.

        Returns:
            Item: A new Quadruple instance.
        """
        position, numbers = QuadrupleBase.extract(board, yaml)
        return cls(board, position, numbers)

    def glyphs(self) -> List[Glyph]:
        """Generate glyphs for the visual representation of the Quadruple.

        Returns:
            List[Glyph]: A list of glyphs representing the quadruple's position and digits.
        """
        return [
            QuadrupleGlyph(class_name=self.__class__.__name__, position=self.position, numbers=self.numbers)
        ]

    def to_dict(self) -> Dict:
        """Convert the Quadruple to a dictionary representation.

        Returns:
            Dict: A dictionary containing the position and digits of the quadruple.
        """
        return {self.__class__.__name__: f"{self.position.row}{self.position.column}={''.join(self.digits)}"}

    def css(self) -> Dict:
        """Return the CSS styling for the Quadruple glyphs.

        Returns:
            Dict: A dictionary defining the CSS styles for the quadruple glyph.
        """
        return {
            ".QuadrupleBaseCircle": {
                "stroke-width": 2,
                "stroke": "black",
                "fill": "white"
            },
            ".QuadrupleBaseText": {
                "stroke": "black",
                "fill": "black",
                "font-size": "30px"
            }
        }
