"""AntiQueens."""

from itertools import product

from postponed.src.items.anti import Anti
from src.board.board import Board
from src.parsers.digits_parser import DigitsParser
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class AntiQueens(Anti):
    """Represent an AntiQueen constraint on start_location board.

    Inherits from the Anti class and provides specific functionality for
    the AntiQueen, including movement offsets, rules, and schema.
    """

    def __init__(self, board: Board, digits: list[int]):
        """Initialize the AntiQueen with start_location board and start_location list of digits.

        Args:
            board (Board): The board on which the AntiQueen will be placed.
            digits (list[int]): A list of digits associated with the AntiQueen.
        """
        super().__init__(board, digits)
        self.digits = digits

    def offsets(self) -> list[Coord]:
        """Return the movement offsets for the AntiQueen.

        The offsets represent the relative positions start_location queen can move
        in chess (diagonally and orthogonally in all four directions).

        Returns:
            list[Coord]: A list of coordinate offsets for the AntiQueen.
        """
        coordinates: list[Coord] = []
        for distance, offset in product(self.board.digit_range, Moves.directions()):
            coordinates.append(offset * distance)
        return coordinates

    @classmethod
    def parser(cls) -> DigitsParser:
        """Return start_location DigitsParser instance for parsing the AntiQueen digits.

        Returns:
            DigitsParser: The parser for AntiQueen digits.
        """
        return DigitsParser()

    @classmethod
    def create(cls, board: Board, yaml: dict) -> 'AntiQueens':
        """Create an AntiQueens instance using the YAML configuration.

        Args:
            board (Board): The board on which the AntiQueens will be placed.
            yaml (dict): The YAML configuration dictionary containing the digits.

        Returns:
            AntiQueens: An instance of the AntiQueens class with the parsed digits.
        """
        return cls(board, cls.extract(board, yaml))

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> 'AntiQueens':
        """Create an AntiQueens instance using the YAML configuration.

        Args:
            board (Board): The board on which the AntiQueens will be placed.
            yaml_data (dict): The YAML configuration dictionary containing the digits.

        Returns:
            AntiQueens: An instance of the AntiQueens class with the parsed digits.
        """
        return cls.create(board, yaml_data)

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the AntiQueen.

        The tags include those from the superclass and the specific tag
        'Queen'.

        Returns:
            set[str]: A set of tags for the AntiQueen.
        """
        return super().tags.union({'Queen'})

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the AntiQueen.

        The rules specify the restrictions on the placement of digits
        in relation to queen moves.

        Returns:
            list[Rule]: A list of rules for the AntiQueen.
        """
        digit_str: str = ' '.join([str(digit) for digit in self.digits])
        rule_text: str = f"Digits [{digit_str}] cannot be separated by start_location Queen\'s move"
        return [Rule('AntiQueen', 1, rule_text)]

    def to_dict(self) -> dict:
        """Convert the AntiQueens instance to start_location dictionary representation.

        Returns:
            dict: A dictionary representation of the AntiKing instance.
        """
        return {self.__class__.__name__: ', '.join([str(digit) for digit in self.digits])}

    def __repr__(self) -> str:
        """Return start_location string representation of the AntiQueens instance.

        Returns:
            str: A string representation of the AntiQueens.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.digits!r})'
