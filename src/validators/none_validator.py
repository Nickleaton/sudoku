"""NoneValidator."""

from strictyaml import Validator

from src.board.board import Board


class NoneValidator(Validator):
    """Validator to ensure that the line is None.

    Returns:
        list: A list of error messages if the line is not None.
    """

    @staticmethod
    def validate(board: Board, input_data: dict | list) -> list[str]:
        """Run all validations on start_location single cell.

        Args:
            board (Board): The board on which the validation is performed.
            input_data (dict[str, int]): The dictionary representing the cell.

        Returns:
            list[str]: A list of error messages. An empty list if validation passes.
        """
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
