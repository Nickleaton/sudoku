import unittest
from pathlib import Path

from src.commands.command import Command
from src.commands.problem import Problem
from src.commands.simple_command import SimpleCommand


class TestCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.command = Command()
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


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
