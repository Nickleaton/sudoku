"""AntiMonkey."""
from src.board.board import Board
from src.items.anti import Anti
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.rule import Rule


class AntiMonkey(Anti):
    """Represents an AntiMonkey constraint on start board.

    Inherits from the Anti class and provides specific functionality for
    the AntiMonkey, including movement offsets, rules.
    """

    def __init__(self, board: Board):
        """Initialize the AntiMonkey with start board.

        Args:
            board (Board): The board on which the AntiMonkey will be placed.
        """
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> list[Coord]:
        """Return the movement offsets for the AntiMonkey.

        The offsets represent the relative positions start monkey can move
        in this game.

        Returns:
            list[Coord]: A list of coordinate offsets for the AntiMonkey.
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
        """Return the tags associated with the AntiMonkey.

        The tags include those from the superclass and the specific tag
        'Monkey'.

        Returns:
            set[str]: A set of tags for the AntiMonkey.
        """
        return super().tags.union({'Monkey'})

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an instance of AntiMonkey from the given board and YAML.

        Args:
            cls: The class of the constraint being created.
            board (Board): The board on which the AntiMonkey will be placed.
            yaml (dict): A dictionary containing configuration data.

        Returns:
            Item: An instance of AntiMonkey.
        """
        return AntiMonkey(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the AntiMonkey.

        The rules specify the restrictions on the placement of digits
        in relation to monkey moves.

        Returns:
            list[Rule]: A list of rules for the AntiMonkey.
        """
        return [
            Rule("AntiMonkey", 1,
                 "Identical digits cannot be separated by start Monkey move [3 forward, 1 to the side]")
        ]

    def __repr__(self) -> str:
        """Return start string representation of the AntiMonkey instance.

        Returns:
            str: A string representation of the AntiMonkey.
        """
        return f"{self.__class__.__name__}({self.board!r})"

    def to_dict(self) -> dict:
        """Convert the AntiMonkey instance to start dictionary representation.

        Returns:
            dict: A dictionary representation of the AntiMonkey.
        """
        return {self.__class__.__name__: None}
