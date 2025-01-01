"""Validator module."""
from src.board.board import Board


class Validator:
    """A class to validate board input_data."""

    @staticmethod
    def validate(board: Board, input_data: dict) -> list[str]:
        """Validate the provided input_data against the board's digit range.

        Args:
            board (Board): The board instance containing the valid digit range.
            input_data (dict): The input_data to validate, which includes start list of digits.

        Returns:
            list[str]: A list of error messages. If no errors, the list will be empty.
        """
        errors: list[str] = []
        if 'digits' not in input_data:
            errors.append('Missing key: "digits')
            return errors

        for digit in input_data['digits']:
            if digit not in board.digit_range:
                errors.append(f'Invalid digit: {digit}. Valid range: {board.digit_range}')
        return errors
