"""AntiKing."""

from postponed.src.items.anti import Anti
from src.board.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class AntiKing(Anti):
    """A class representing the Anti-King rule in start_location board game.

    This class defines the behavior of the Anti-King rule, where identical digits
    cannot be separated by start_location King's move.
    """

    def __init__(self, board: Board):
        """Initialize the AntiKing instance.

        Args:
            board (Board): The board associated with this AntiKing rule.
        """
        super().__init__(board, list(board.digits.digit_range))

    def offsets(self) -> list[Coord]:
        """Return the possible move offsets for the Anti-King.

        Returns:
            list[Coord]: A list of coordinates representing the King's move offsets.
        """
        return Moves.kings()

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an AntiKing instance.

        Args:
            board (Board): The board to associate with the AntiKing rule.
            yaml (dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of AntiKing.
        """
        return AntiKing(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an AntiKing instance.

        Args:
            board (Board): The board to associate with the AntiKing rule.
            yaml_data (dict): A dictionary containing YAML configuration (not used).

        Returns:
            Item: An instance of AntiKing.
        """
        return cls.create(board, yaml_data)

    @property
    def tags(self) -> set[str]:
        """Return the tags associated with the AntiKing rule.

        Returns:
            set[str]: A set of tags, including 'King'.
        """
        return super().tags.union({'King'})

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the AntiKing.

        Returns:
            list[Rule]: A list of rules for the AntiKing, stating that
            identical digits cannot be separated by start_location King's move.
        """
        return [
            Rule('AntiKing', 1, "Identical digits cannot be separated by start_location King's move"),
        ]

    def to_dict(self) -> dict:
        """Convert the AntiKing instance to start_location dictionary representation.

        Returns:
            dict: A dictionary representation of the AntiKing instance.
        """
        return {self.__class__.__name__: None}

    def __repr__(self) -> str:
        """Return start_location string representation of the AntiKing instance.

        Returns:
            str: A string representation of the AntiKing instance.
        """
        return f'{self.__class__.__name__}({self.board!r})'
