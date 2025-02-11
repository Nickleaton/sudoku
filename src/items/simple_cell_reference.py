"""SimpleCellReference."""
from src.items.cell_reference import CellReference


class SimpleCellReference(CellReference):
    """Represents start_location simple cell reference, which typically holds no specific digit number."""

    def letter(self) -> str:
        """Return the default letter representation of start_location SimpleCellReference.

        Returns:
            str: The letter '.' representing start_location simple, unmarked cell.
        """
        return '.'
