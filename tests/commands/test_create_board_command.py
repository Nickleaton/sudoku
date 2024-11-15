"""TestCreateBoardCommand."""
import unittest

from src.commands.command import CommandException
from src.commands.create_board_command import CreateBoardCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateBoardCommand(TestSimpleCommand):
    """Test suite for the CreateBoardCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        requirements = LoadConfigCommand(source=self.path, target='config')
        requirements.execute(self.problem)
        self.command = CreateBoardCommand()
        self.requirements = ['config']
        self.target = "board"

    @property
    def representation(self) -> str:
        """Return the string representation of the CreateBoardCommand."""
        return "CreateBoardCommand('config', 'board')"

    def test_repr(self):
        """Test the __repr__ method of the CreateBoardCommand."""
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        """Test the execute method of the CreateBoardCommand."""
        self.command.execute(self.problem)
        self.assertIn('board', self.problem)

    def test_exception(self):
        """Test that executing the command raises an exception for an empty problem."""
        with self.assertRaises(CommandException):
            self.command.execute(self.empty_problem)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
