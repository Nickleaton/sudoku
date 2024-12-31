"""Validator Module."""
from src.board.board import Board


class Validator:
    """Base class for board validation.

    This class provides a base structure for validators that check
    the validity of the start `Board` against some `input_data`. It can be extended
    by custom validators for specific types of validation.
    """

    @staticmethod
    def validate_keys(input_data: dict, required_keys: list) -> list:
        """Validate the required keys in the input_data dictionary.

        Args:
            input_data (dict): The input_data dictionary to validate.
            required_keys (list): The list of keys that must be present in the input_data.

        Returns:
            list: A list of error messages if any required keys are missing.
        """
        return [f'Missing key: "{key}"' for key in required_keys if key not in input_data]

    @staticmethod
    def validate(board: Board, input_data: dict) -> list:
        """Validate the provided input_data dictionary against the board.

        This method is intended to be overridden by subclasses to
        implement specific validation logic. By default, it returns
        an empty list, indicating that no validation errors were found.

        Args:
            board (Board): The board to validate against.
            input_data (dict): The input_data to validate.

        Returns:
            list: A list of error messages. If no validation errors
            are found, an empty list is returned.
        """
        return []

    def __repr__(self) -> str:
        """Return string representation of the Validator class.

        Returns:
            str: A string representation of the class, including its name.
        """
        return f'{self.__class__.__name__}()'
