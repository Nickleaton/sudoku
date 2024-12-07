"""Validator module."""
from src.items.board import Board


class Validator:
    """A class to validate board data."""

    @staticmethod
    def validate(board: Board, data: dict) -> list[str]:
        """
        Validate the provided data against the board's digit range.

        Args:
            board (Board): The board instance containing the valid digit range.
            data (dict): The data to validate, which includes a list of digits.

        Returns:
            list[str]: A list of error messages. If no errors, the list will be empty.
        """
        errors: list[str] = []
        if 'digits' not in data:
            errors.append("Missing key: 'digits'")
            return errors

        for digit in data['digits']:
            if digit not in board.digit_range:
                errors.append(f"Invalid digit: {digit}. Valid range: {board.digit_range}")
        return errors
