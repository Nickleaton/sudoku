from typing import List, Dict

from src.items.anti import Anti
from src.items.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiKnight(Anti):
    """Represents an AntiKnight item on a board.

    Inherits from the Anti class and provides specific functionality for
    the AntiKnight, including movement offsets, rules
    """

    def __init__(self, board: Board):
        """Initialize the AntiKnight with a board.

        Args:
            board (Board): The board on which the AntiKnight will be placed.
        """
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> List[Coord]:
        """Return the movement offsets for the AntiKnight.

        The offsets represent the relative positions a knight can move
        in chess.

        Returns:
            List[Coord]: A list of coordinate offsets for the AntiKnight.
        """
        return [
            Coord(-1, -2),
            Coord(1, -2),
            Coord(-2, -1),
            Coord(-2, 1),
            Coord(-1, 2),
            Coord(1, 2),
            Coord(2, 1),
            Coord(2, -1)
        ]

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the AntiKnight.

        The tags include those from the superclass and the specific tag
        'Knight'.

        Returns:
            set[str]: A set of tags for the AntiKnight.
        """
        return super().tags.union({'Knight'})

    @classmethod
    def create(cls, board: Board, yaml: Dict) -> Item:
        """Create an instance of AntiKnight from the given board and YAML.

        Args:
            cls: The class of the item being created.
            board (Board): The board on which the AntiKnight will be placed.
            yaml (Dict): A dictionary containing configuration data.

        Returns:
            Item: An instance of AntiKnight.
        """
        return AntiKnight(board)

    @property
    def rules(self) -> List[Rule]:
        """Return the rules associated with the AntiKnight.

        The rules specify the restrictions on the placement of digits
        in relation to knight moves.

        Returns:
            List[Rule]: A list of rules for the AntiKnight.
        """
        return [
            Rule("AntiKnight", 1, "Identical digits cannot be separated by a knight's move")
        ]

    def __repr__(self) -> str:
        """Return a string representation of the AntiKnight instance.

        Returns:
            str: A string representation of the AntiKnight.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> Dict:
        """Convert the AntiKnight instance to a dictionary representation.

        Returns:
            Dict: A dictionary representation of the AntiKnight.
        """
        return {self.__class__.__name__: None}
