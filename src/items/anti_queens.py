"""AntiQueens."""
from typing import list, dict

from src.items.anti import Anti
from src.items.board import Board
from src.parsers.digits_parser import DigitsParser
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiQueens(Anti):
    """Represent an AntiQueen item on a board.

    Inherits from the Anti class and provides specific functionality for
    the AntiQueen, including movement offsets, rules, and schema.
    """

    def __init__(self, board: Board, digits: list[int]):
        """Initialize the AntiQueen with a board and a list of digits.

        Args:
            board (Board): The board on which the AntiQueen will be placed.
            digits (list[int]): A list of digits associated with the AntiQueen.
        """
        super().__init__(board, digits)
        self.digits = digits

    def offsets(self) -> list[Coord]:
        """Return the movement offsets for the AntiQueen.

        The offsets represent the relative positions a queen can move
        in chess (diagonally in all four directions).

        Returns:
            list[Coord]: A list of coordinate offsets for the AntiQueen.
        """
        results: list[Coord] = []
        for distance in self.board.digit_range:
            results.append(Coord(-1, -1) * distance)  # Move diagonally up-left
            results.append(Coord(1, -1) * distance)  # Move diagonally up-right
            results.append(Coord(-1, 1) * distance)  # Move diagonally down-left
            results.append(Coord(1, 1) * distance)  # Move diagonally down-right
        return results

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
        digit_str = ' '.join([str(digit) for digit in self.digits])
        return [
            Rule("AntiQueen", 1, f"Digits [{digit_str}] cannot be separated by a Queen's move")
        ]

    @classmethod
    def parser(cls) -> DigitsParser:
        """Return a DigitsParser instance for parsing the AntiQueen digits.

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
        lst = cls.extract(board, yaml)
        return cls(board, lst)

    def __repr__(self) -> str:
        """Return a string representation of the AntiQueens instance.

        Returns:
            str: A string representation of the AntiQueens.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"
