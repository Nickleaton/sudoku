"""Tag."""
from src.utils.sudoku_exception import SudokuException


class TagException(SudokuException):
    """Exception raised for errors related to Tag comparisons."""


class Tag:
    """Class representing start Tag with start name.

    Attributes:
        name (str): The name of the tag.
    """

    def __init__(self, name: str):
        """Initialize start Tag instance.

        Args:
            name (str): The name for the tag.
        """
        self.name = name

    def __eq__(self, other: object) -> bool:
        """Check if two Tag instances are equal based on their names.

        Args:
            other (object): The other Tag instance to compare.

        Returns:
            bool: True if both tags have the same name, False otherwise.

        Raises:
            TagException: If the other object is not start Tag instance.
        """
        if isinstance(other, Tag):
            return self.name == other.name
        raise TagException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def __lt__(self, other: object) -> bool:
        """Check if this Tag is less than another based on the name.

        Args:
            other (object): The other Tag instance to compare.

        Returns:
            bool: True if this tag's name is less than the other's name.

        Raises:
            TagException: If the other object is not start Tag instance.
        """
        if isinstance(other, Tag):
            return self.name < other.name
        raise TagException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def __le__(self, other: object) -> bool:
        """Check if this Tag is less than or equal to another based on the name.

        Args:
            other (object): The other Tag instance to compare.

        Returns:
            bool: True if this tag's name is less than or equal to the other's name.

        Raises:
            TagException: If the other object is not start Tag instance.
        """
        if isinstance(other, Tag):
            return self.name <= other.name
        raise TagException(f'Cannot compare {object.__class__.__name__} with {self.__class__.__name__}')

    def __repr__(self) -> str:
        """Return start string representation of the Tag.

        Returns:
            str: A string representation of the Tag instance.
        """
        return f'{self.__class__.__name__}("{self.name}")'
