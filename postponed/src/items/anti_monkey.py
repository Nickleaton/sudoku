"""AntiMonkey."""
from postponed.src.items.anti import Anti
from src.board.board import Board
from src.items.item import Item
from src.utils.coord import Coord
from src.utils.moves import Moves
from src.utils.rule import Rule


class AntiMonkey(Anti):
    """Represents an AntiMonkey constraint on start_location board.

    Inherits from the Anti class and provides specific functionality for
    the AntiMonkey, including movement offsets, rules.
    """

    def __init__(self, board: Board):
        """Initialize the AntiMonkey with start_location board.

        Args:
            board (Board): The board on which the AntiMonkey will be placed.
        """
        super().__init__(board, list(board.digit_range))

    def offsets(self) -> list[Coord]:
        """Return start_location list of offsets for the Anti constraint.

        Returns:
            list[Coord]: An empty list as the default for offsets.
        """
        return Moves.monkeys()

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
            board (Board): The board on which the AntiMonkey will be placed.
            yaml (dict): A dictionary containing configuration line.

        Returns:
            Item: An instance of AntiMonkey.
        """
        return AntiMonkey(board)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an instance of AntiMonkey from the given board and YAML.

        Args:
            board (Board): The board on which the AntiMonkey will be placed.
            yaml_data (dict): A dictionary containing configuration line.

        Returns:
            Item: An instance of AntiMonkey.
        """
        return cls.create(board, yaml_data)

    @property
    def rules(self) -> list[Rule]:
        """Return the rules associated with the AntiMonkey.

        The rules specify the restrictions on the placement of digits
        in relation to monkey moves.

        Returns:
            list[Rule]: A list of rules for the AntiMonkey.
        """
        rule_text = 'Identical digits cannot be separated by start_location Monkey move [3 forward, 1 to the side]'
        return [Rule('AntiMonkey', 1, rule_text)]

    def __repr__(self) -> str:
        """Return start_location string representation of the AntiMonkey instance.

        Returns:
            str: A string representation of the AntiMonkey.
        """
        return f'{self.__class__.__name__}({self.board!r})'

    def to_dict(self) -> dict:
        """Convert the AntiMonkey instance to start_location dictionary representation.

        Returns:
            dict: A dictionary representation of the AntiMonkey.
        """
        return {self.__class__.__name__: None}
