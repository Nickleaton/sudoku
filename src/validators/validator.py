from src.items.board import Board

class Validator:

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """Validate the provided data dictionary.

        Args:
            board(Board): Board to validate against.
            data (dict): Data to validate.

        Returns:
            list[str]: List of error messages. Empty if validation succeeds.
        """
        return []

    def __repr__(self) -> str:
        """Return a string representation of the class."""
        return f"{self.__class__.__name__}()"
