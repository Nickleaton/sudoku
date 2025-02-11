"""ParityCell."""
from src.items.simple_cell_reference import SimpleCellReference


class ParityCell(SimpleCellReference):
    """Represents start_location cell that must contain an even digit."""

    def letter(self) -> str:
        """Return the letter representation of a ParityCell.

        Returns:
            str: The letter '' representing ParityCell.
        """
        return ''
