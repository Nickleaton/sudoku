"""FPuzzlesDumper."""
from src.board.board import Board
from src.load_dump.dumper import Dumper


class FPuzzlesDumper(Dumper):
    """A Dumper subclass that formats the board for FPuzzles-specific output.

    This class implements the abstract method `text()` from the Dumper class to
    generate a textual representation of the board in the format expected by FPuzzles.

    Attributes:
        board (Board): The board instance to be dumped.
    """

    def __init__(self, board: Board):
        """Initialize the FPuzzlesDumper with a board instance.

        Args:
            board (Board): The board instance to be dumped.
        """
        super().__init__(board)

    def text(self) -> str:
        """Generate a textual representation of the board in the format expected by FPuzzles.

        Returns:
            str: The formatted board in the FPuzzles-specific format.
        """
        return "xxx"
