"""TestCommand."""
import unittest
from pathlib import Path

from src.commands.command import Command, CommandException
from src.commands.problem import Problem


class TestCommand(unittest.TestCase):
    """Test suite for the Command class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.command = Command()
        self.problem = Problem()
        self.empty_problem = Problem()
        self.path = Path('problems\\easy\\problem001.yaml')
        self.requirements = []
        self.target = ""

    def test_command(self):
        """Test the execution of the Command."""
        if self.command is None:
            return
        self.command.execute(self.problem)
        if self.__class__.__name__ == 'TestCommand':
            self.assertEqual(self.command.name, 'Command')
        else:
            name = self.__class__.__name__.replace("Test", "").replace("Command", "")
            self.assertEqual(self.command.name, name)

    @property
    def representation(self) -> str:
        """Return the string representation of the command."""
        return f"{self.command.__class__.__name__}()"

    def test_repr(self):
        """Test the __repr__ method of the Command."""
        if self.command is None:
            return
        self.assertEqual(self.representation, repr(self.command))

    def test_preconditions(self):
        """Test the precondition checks of the Command."""
        problem = Problem()
        for requirement in self.requirements:
            with self.assertRaises(CommandException):
                self.command.precondition_check(problem)
            problem[requirement] = ""
        self.command.precondition_check(problem)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
