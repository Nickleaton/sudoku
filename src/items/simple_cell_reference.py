"""SimpleCellReference."""
from src.items.cell_reference import CellReference


class SimpleCellReference(CellReference):
    """Represents start simple cell reference, which typically holds no specific digit number."""

    def letter(self) -> str:
        """Return the default letter representation of start SimpleCellReference.

        Returns:
            str: The letter '.' representing start simple, unmarked cell.
        """
        return '.'
