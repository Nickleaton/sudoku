from src.items.cell_reference import CellReference


class SimpleCellReference(CellReference):
    """Represents a simple cell reference, which typically holds no specific digit value."""

    def letter(self) -> str:
        """Return the default letter representation of a SimpleCellReference.

        Returns:
            str: The letter '.' representing a simple, unmarked cell.
        """
        return '.'
