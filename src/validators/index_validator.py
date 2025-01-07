"""IndexValidator."""
from src.board.board import Board
from src.validators.validator import Validator


class IndexValidator(Validator):
    """Validator for the 'Index' key in input data."""

    @staticmethod
    def validate(board: Board, input_data: dict[str, int | str]) -> list[str]:
        """Validate the 'Index' key in the input data.

        Args:
            board (Board): The Sudoku board that the constraint applies to.
            input_data (dict[str, object]): A dictionary containing the 'Index' key to validate.

        Returns:
            list[str]: A list of error messages, or an empty list if the input is valid.
        """
        errors: list[str] = []

        # Ensure the input contains only the 'Index' key
        if len(input_data) != 1 or 'Index' not in input_data:
            errors.append(f"Invalid input data: {input_data!r}. Expected a single 'Index' key.")
            return errors

        # Validate the 'Index' number
        index = input_data['Index']
        try:
            index = int(index)
        except (ValueError, TypeError):
            errors.append(f"'Index' must be an integer, got {type(index).__name__}: {index!r}.")
        else:
            if index < 0:
                errors.append(f"'Index' must be a non-negative integer, got {index!r}.")

        return errors
