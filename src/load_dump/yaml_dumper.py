"""YamlDumper."""
from src.board.board import Board
from src.load_dump.dumper import Dumper


class YamlDumper(Dumper):
    """Dumper subclass that formats the board for YAML-specific output.

    This class implements the abstract method `text()` from the Dumper class to
    generate a textual representation of the board in YAML format.

    Attributes:
        board (Board): The board instance to be dumped.
    """

    def __init__(self, board: Board):
        """Initialize the YamlDumper with a board instance.

        Args:
            board (Board): The board instance to be dumped.
        """
        super().__init__(board)

    def text(self) -> str:
        """Return text for the dumper."""
        return ""
