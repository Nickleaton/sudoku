from typing import List, Dict

import strictyaml

from src.items.anti import Anti
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.direction import Direction
from src.utils.rule import Rule


class AntiKing(Anti):
    """A class representing the Anti-King rule in a board game.

    This class defines the behavior of the Anti-King rule, where identical digits
    cannot be separated by a King's move.
    """

    def __init__(self, board: Board):
        """Initializes the AntiKing instance.

        Args:
            board (Board): The board associated with this AntiKing rule.
        """
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Coord]:
        """Returns the possible move offsets for the Anti-King.

        Returns:
            List[Coord]: A list of coordinates representing the King's move offsets.
        """
        return Direction.kings()

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Creates an AntiKing instance.

        Args:
            cls: The class itself (AntiKing).
            board (Board): The board to associate with the AntiKing rule.
            yaml (Dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of AntiKing.
        """
        return AntiKing(board)

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with the AntiKing rule.

        Returns:
            set[str]: A set of tags, including 'King'.
        """
        return super().tags.union({'King'})

    @property
    def rules(self) -> List[Rule]:
        """Returns the rules associated with the AntiKing.

        Returns:
            List[Rule]: A list of rules for the AntiKing, stating that
            identical digits cannot be separated by a King's move.
        """
        return [
            Rule("AntiKing", 1, "Identical digits cannot be separated by a King's move")
        ]

    def schema(self) -> Dict:
        """Returns the schema for the AntiKing.

        Returns:
            Dict: A dictionary representing the schema for the AntiKing.
        """
        return {strictyaml.Optional('Antiking'): None}

    def __repr__(self) -> str:
        """Returns a string representation of the AntiKing instance.

        Returns:
            str: A string representation of the AntiKing instance.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        """Converts the AntiKing instance to a dictionary representation.

        Returns:
            Dict: A dictionary representation of the AntiKing instance.
        """
        return {self.__class__.__name__: None}
