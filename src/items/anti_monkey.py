from typing import List, Dict

import strictyaml

from src.items.anti import Anti
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiMonkey(Anti):
    """Represents an AntiMonkey item on a board.

    Inherits from the Anti class and provides specific functionality for
    the AntiMonkey, including movement offsets, rules, and schema.
    """

    def __init__(self, board: Board):
        """Initializes the AntiMonkey with a board.

        Args:
            board (Board): The board on which the AntiMonkey will be placed.
        """
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Coord]:
        """Returns the movement offsets for the AntiMonkey.

        The offsets represent the relative positions a monkey can move
        in this game.

        Returns:
            List[Coord]: A list of coordinate offsets for the AntiMonkey.
        """
        return [
            Coord(-1, -3),
            Coord(1, -3),
            Coord(-3, -1),
            Coord(-3, 1),
            Coord(-1, 3),
            Coord(1, 3),
            Coord(3, 1),
            Coord(3, -1)
        ]

    @property
    def tags(self) -> set[str]:
        """Returns the tags associated with the AntiMonkey.

        The tags include those from the superclass and the specific tag
        'Monkey'.

        Returns:
            set[str]: A set of tags for the AntiMonkey.
        """
        return super().tags.union({'Monkey'})

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Creates an instance of AntiMonkey from the given board and YAML.

        Args:
            cls: The class of the item being created.
            board (Board): The board on which the AntiMonkey will be placed.
            yaml (Dict): A dictionary containing configuration data.

        Returns:
            Item: An instance of AntiMonkey.
        """
        return AntiMonkey(board)

    @property
    def rules(self) -> List[Rule]:
        """Returns the rules associated with the AntiMonkey.

        The rules specify the restrictions on the placement of digits
        in relation to monkey moves.

        Returns:
            List[Rule]: A list of rules for the AntiMonkey.
        """
        return [
            Rule("AntiMonkey", 1, "Identical digits cannot be separated by a Monkey move [3 forward, 1 to the side]")
        ]

    def schema(self) -> Dict:
        """Returns the schema for the AntiMonkey.

        The schema defines the expected structure of data for the
        AntiMonkey item.

        Returns:
            Dict: A dictionary representing the schema for the AntiMonkey.
        """
        return {strictyaml.Optional('AntiMonkey'): None}

    def __repr__(self) -> str:
        """Returns a string representation of the AntiMonkey instance.

        Returns:
            str: A string representation of the AntiMonkey.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        """Converts the AntiMonkey instance to a dictionary representation.

        Returns:
            Dict: A dictionary representation of the AntiMonkey.
        """
        return {self.__class__.__name__: None}
