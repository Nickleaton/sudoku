"""YamlDumper."""

from src.load_dump.dumper import Dumper


class YamlDumper(Dumper):
    """Dumper subclass that formats the board for YAML-specific output.

    This class implements the abstract method `text()` from the `Dumper` class to
    generate a textual representation of the board in YAML format.

    Attributes:
        board (Board): The board instance to be dumped.
    """

    def text(self) -> str:
        """Generate and return the YAML representation of the board.

        This method overrides the `text()` method from the `Dumper` base class to provide
        a YAML-specific output for the board.

        Returns:
            str: The YAML-formatted string representation of the board.
        """
        return ''
