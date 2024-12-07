"""Validator."""
from src.items.board import Board


class Validator:
    """Base class for board validation.

    This class provides a base structure for validators that check
    the validity of a `Board` against some data. It can be extended
    by custom validators for specific types of validation.
    """

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate the provided data dictionary against the board.

        This method is intended to be overridden by subclasses to
        implement specific validation logic. By default, it returns
        an empty list, indicating that no validation errors were found.

        Args:
            board (Board): The board to validate against.
            data (dict): The data to validate.

        Returns:
            list[str]: A list of error messages. If no validation errors
            are found, an empty list is returned.
        """
        return []

    def __repr__(self) -> str:
        """Return a string representation of the Validator class.

        Returns:
            str: A string representation of the class, including its name.
        """
        return f"{self.__class__.__name__}()"
