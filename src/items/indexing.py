"""Indexing."""
from src.board.board import Board
from src.items.item import Item
from src.items.standard_region import StandardRegion
from src.parsers.digits_parser import DigitsParser
from src.utils.rule import Rule


class Indexer(StandardRegion):
    """Represent an indexing mechanism within a standard region on the board.

    Inherits from StandardRegion to define regions that handle indexing logic,
    including parsing digits and extracting relevant data for further processing.
    """

    @classmethod
    def parser(cls) -> DigitsParser:
        """Return the parser used for extracting digit-related information.

        Returns:
            DigitsParser: An instance of the DigitsParser class used for parsing digits.
        """
        return DigitsParser()

    @classmethod
    def extract(cls, board: Board, yaml: dict) -> int:
        """Extract the index from the provided YAML configuration.

        Args:
            board (Board): The board object on which the index will be applied.
            yaml (dict): The YAML configuration containing the index value.

        Returns:
            int: The extracted index value from the YAML configuration.
        """
        return int(yaml[cls.__name__])

    @classmethod
    def create(cls, board: Board, yaml: dict) -> Item:
        """Create an Indexer instance from the provided board and YAML data.

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
        return cls.create(board, yaml_data)

    @staticmethod
    def variant() -> str:
        """Return the variant type associated with this Indexer.

        Returns:
            str: An empty string, to be potentially overridden by subclasses.
        """
        return ""

    @staticmethod
    def other_variant() -> str:
        """Return the other variant type associated with this Indexer.

        Returns:
            str: An empty string, to be potentially overridden by subclasses.
        """
        return ""

    def __repr__(self) -> str:
        """Return a string representation of the Indexer instance.

        Returns:
            str: The string representation of the Indexer with board and index.
        """
        return f"{self.__class__.__name__}({self.board!r}, {self.index!r})"

    @property
    def rules(self) -> list[Rule]:
        """Return a list of rules associated with this Indexer.

        Returns:
            list[Rule]: A list of Rule instances that describe the constraints
            and logic related to the indexing region.
        """
        return [
            Rule(
                f'{self.__class__.__name__}{self.index}',
                1,
                (
                    f"Digits in {self.variant()} {self.index} indicate the {self.variant()} "
                    f"in which the digit {self.index} appears in that {self.other_variant()}"
                )
            )
        ]

    @property
    def tags(self) -> set[str]:
        """Return a set of tags associated with this Indexer.

        Returns:
            set[str]: A set of tags, including 'Indexing', combined with any tags
            from the superclass.
        """
        return super().tags.union({'Indexing'})
