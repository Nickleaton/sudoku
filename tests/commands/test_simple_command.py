import unittest
from pathlib import Path

from src.commands.command import Command
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand
from tests.commands.test_command import TestCommand


class TestSimpleCommand(TestCommand):

    def setUp(self) -> None:
        self.command = SimpleCommand()
        self.problem = Problem()
        self.empty_problem = Problem()
        self.path = Path('problems\\easy\\problem001.yaml')

    def test_command(self):
        self.command.execute(self.problem)
        if self.__class__.__name__ == 'TestCommand':
            self.assertEqual(self.command.name, 'Command')
        else:
            name = self.__class__.__name__.replace("Test", "").replace("Command", "")
            self.assertEqual(self.command.name, name)

    @property
    def representation(self) -> str:
        return f"{self.command.__class__.__name__}()"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_multiple_commands(self):
        other1 = SimpleCommand()
        other2 = SimpleCommand()
        composed = other1 | other2
        self.assertIn(other1, composed.items)
        self.assertIn(other2, composed.items)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
