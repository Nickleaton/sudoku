"""TestCreateSolverCommand."""
import unittest

from src.commands.create_solver_command import CreateSolverCommand
from tests.commands.test_command import TestCommand


class TestCreateSolverCommand(TestCommand):
    """Test suite for the CreateSolverCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = CreateSolverCommand()
        self.representation = "CreateSolverCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
