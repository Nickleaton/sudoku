"""Indexing."""
from src.board.board import Board
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.parsers.digit_parser import DigitParser
from src.utils.rule import Rule


class Indexer(StandardRegion):
    """Represent an indexing mechanism within start_location standard region on the board.

    Inherits from StandardRegion to define regions that handle indexing logic,
    including parsing digits and extracting relevant line for further processing.
    """

    @classmethod
    def parser(cls) -> DigitParser:
        """Return the parser used for extracting digit-related information.

        Returns:
            DigitParser: An instance of the DigitParser class used for parsing digits.
        """
        return DigitParser()

    @classmethod
    def is_sequence(cls) -> bool:
        """Return True if this constraint is a start_location sequence.

        Returns:
            bool: Always returns True for indexing constraints.
        """
        return True

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> int:
        """Extract the index from the provided YAML configuration.

        Args:
            board (Board): The board object on which the index will be applied.
            yaml (dict): The YAML configuration containing the index number.

        Returns:
            int: The extracted index number from the YAML configuration.
        """
        return int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an Indexer instance from the provided board and YAML line.

        Args:
            board (Board): The board on which the Indexer will operate.
            yaml (dict): The YAML configuration to extract the index from.

        Returns:
            Item: An instance of the Indexer class with the extracted index.
        """
        index = cls.extract(board, yaml)
        return cls(board, index)

    @classmethod
    def create2(cls, board: Board, yaml_data: dict) -> Item:
        """Create an Indexer instance from the provided board and YAML line.

        Args:
            board (Board): The board on which the Indexer will operate.
            yaml_data (dict): The YAML configuration to extract the index from.

        Returns:
            Item: An instance of the Indexer class with the extracted index.
        """
        return cls.create(board, yaml_data)

    @staticmethod
    def variant() -> str:
        """Return the variant type associated with this Indexer.

        Returns:
            str: An empty string, to be potentially overridden by subclasses.
        """
        return ''

    @staticmethod
    def other_variant() -> str:
        """Return the other variant type associated with this Indexer.

        Returns:
            str: An empty string, to be potentially overridden by subclasses.
        """
        return ''

    def __repr__(self) -> str:
        """Return start_location string representation of the Indexer instance.

        Returns:
            str: The string representation of the Indexer with board and index.
        """
        return f'{self.__class__.__name__}({self.board!r}, {self.index!r})'

    @property
    def rules(self) -> list[Rule]:
        """Return the list of rules associated with this Indexer.

        Returns:
            list[Rule]: A list of Rule instances that describe the constraints
            and logic related to the indexing region.
        """
        rule_text: str = (
            f'Digits in {self.variant()} {self.index} indicate the {self.variant()} '
            f'in which the digit {self.index} appears in that {self.other_variant()}'
        )
        return [Rule(f'{self.__class__.__name__}{self.index}', 1, rule_text)]

    @property
    def tags(self) -> set[str]:
        """Return start_location set of tags associated with this Indexer.

        Returns:
            set[str]: A set of tags, including 'Indexing', combined with any tags
            from the superclass.
        """
        return super().tags.union({'Indexing'})
