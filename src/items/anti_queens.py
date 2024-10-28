from typing import List, Dict

from src.items.anti import Anti
from src.items.board import Board
from src.parsers.digits_parser import DigitsParser
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiQueens(Anti):
    """Represents an AntiQueen item on a board.

    Inherits from the Anti class and provides specific functionality for
    the AntiQueen, including movement offsets, rules, and schema.
    """

    def __init__(self, board: Board, digits: List[int]):
        """Initializes the AntiQueen with a board and a list of digits.

        Args:
            board (Board): The board on which the AntiQueen will be placed.
            digits (List[int]): A list of digits associated with the AntiQueen.
        """
        super().__init__(board, digits)
        self.digits = digits

    def offsets(self) -> List[Coord]:
        """Returns the movement offsets for the AntiQueen.

        The offsets represent the relative positions a queen can move
        in chess (diagonally in all four directions).

        Returns:
            List[Coord]: A list of coordinate offsets for the AntiQueen.
        """
        results: List[Coord] = []
        for distance in self.board.digit_range:
            results.append(Coord(-1, -1) * distance)  # Move diagonally up-left
            results.append(Coord(1, -1) * distance)  # Move diagonally up-right
            results.append(Coord(-1, 1) * distance)  # Move diagonally down-left
            results.append(Coord(1, 1) * distance)  # Move diagonally down-right
        return results

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with the AntiQueen.

        The tags include those from the superclass and the specific tag
        'Queen'.

        Returns:
            set[str]: A set of tags for the AntiQueen.
        """
        return super().tags.union({'Queen'})

    @property
    def rules(self) -> List[Rule]:
        """Returns the rules associated with the AntiQueen.

        The rules specify the restrictions on the placement of digits
        in relation to queen moves.

        Returns:
            List[Rule]: A list of rules for the AntiQueen.
        """
        digit_str = ' '.join([str(digit) for digit in self.digits])
        return [
            Rule("AntiQueen", 1, f"Digits [{digit_str}] cannot be separated by a Queen's move")
        ]

    @classmethod
    def parser(cls) -> DigitsParser:
        return DigitsParser()

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> 'AntiQueens':
        lst = cls.extract(board, yaml)
        return cls(board, lst)

    def __repr__(self) -> str:
        """Returns a string representation of the AntiQueens instance.

        Returns:
            str: A string representation of the AntiQueens.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.digits!r})"