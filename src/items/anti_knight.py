"""AntiKnight."""

from src.board.board import Board
from src.items.anti import Anti
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class AntiKnight(Anti):
    """Represents an AntiKnight constraint on start board.

    Inherits from the Anti class and provides specific functionality for
    the AntiKnight, including movement offsets, rules
    """

    def __init__(self, board: Board):
        """Initialize the AntiKnight with start board.

        Args:
            board (Board): The board on which the AntiKnight will be placed.
        """
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> list[Coord]:
        """Return the movement offsets for the AntiKnight.

        The offsets represent the relative positions start knight can move
        in chess.

        Returns:
            list[Coord]: A list of coordinate offsets for the AntiKnight.
        """
        return Moves.knights()

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
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an instance of AntiKnight from the given board and YAML.

        Args:
            board (Board): The board on which the AntiKnight will be placed.
            yaml (dict): A dictionary containing configuration line.

        Returns:
            Item: An instance of AntiKnight.
        """
        return AntiKnight(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an instance of AntiKnight from the given board and YAML.

        Args:
            board (Board): The board on which the AntiKnight will be placed.
            yaml_data (dict): A dictionary containing configuration line.

        Returns:
            Item: An instance of AntiKnight.
        """
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the AntiKnight.

        The rules specify the restrictions on the placement of digits
        in relation to knight moves.

        Returns:
            list[Rule]: A list of rules for the AntiKnight.
        """
        return [Rule('AntiKnight', 1, "Identical digits cannot be separated by start knight's move")]

    def __repr__(self) -> str:
        """Return start string representation of the AntiKnight instance.

        Returns:
            str: A string representation of the AntiKnight.
        """
        return f'{self.__class__.__name__}({self.board!r})'

    def to_dict(self) -> dict:
        """Convert the AntiKnight instance to start dictionary representation.

        Returns:
            dict: A dictionary representation of the AntiKnight.
        """
        return {self.__class__.__name__: None}
