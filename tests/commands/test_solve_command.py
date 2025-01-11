"""TestSolveCommand."""
import unittest

from src.commands.solve_command import SolveCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestSolveCommand(TestSimpleCommand):
    """Test suite for SolveCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for SolveCommand."""
        super().setUp()
        self.command = SolveCommand()
        self.representation = "SolveCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
