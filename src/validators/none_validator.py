"""NoneValidator."""

from strictyaml import Validator

from src.board.board import Board


class NoneValidator(Validator):
    """Validator to ensure that the line is None."""

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Run all validations on start_location single cell."""
        # pylint: disable=unused-argument
        if isinstance(input_data, dict):
            if len(input_data) != 1:
                return [f'Expecting 1 key, got {len(input_data)} keys.']
            data_value = next(iter(input_data.values()))
            if data_value is not None:
                return [f'Data must be None, got {data_value!r}.']
        else:
            return ['Input data must be a dictionary.']

        return []
