from typing import List, Tuple

from src.validators.cell_validator import CellValidator
from src.validators.validator import Validator


class LineValidator(Validator):

    @staticmethod
    def validate(board: 'Board', data: List[dict]) -> List[str]:
        """Validate that all cells in the answer are valid, connected by a king's move, and unique.

        Args:
            board (Board): The board on which the validation is performed.
            data (list[dict]): A list of dictionaries containing cell coordinates to validate.
                Each dictionary must have 'row' and 'column' keys.

        Returns:
            list[str]: A list of error messages. Empty if validation passes.
        """
        if not data:
            return ["The data cannot be empty."]

        errors: List[str] = []
        seen_cells: set[Tuple[int, int]] = set()

        # Validate cells using CellValidator
        for i, cell in enumerate(data):
            # Validate cell keys, range, and uniqueness
            errors.extend(CellValidator.has_valid_keys(cell))
            errors.extend(CellValidator.validate_range(board, cell))

            row, col = cell['row'], cell['column']
            cell_tuple = (row, col)

            # Check for duplicate cells
            if cell_tuple in seen_cells:
                errors.append(f"Duplicate cell found: ({row}, {col})")
            seen_cells.add(cell_tuple)

        # Validate connectivity by king's move using CellValidator
        for i in range(len(data) - 1):
            errors.extend(CellValidator.validate_connected(data[i], data[i + 1]))

        return errors


if __name__ == "__main__":
    unittest.main()
