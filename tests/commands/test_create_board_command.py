import unittest

from src.commands.command import CommandException
from src.commands.create_board_command import CreateBoardCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateBoardCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(source=self.path, target='config')
        requirements.execute(self.problem)
        self.command = CreateBoardCommand()
        self.requirements = ['config']
        self.target = "board"

    @property
    def representation(self) -> str:
        return "CreateBoardCommand('config', 'board')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        self.command.execute(self.problem)
        self.assertIn('board', self.problem)

    def test_exception(self):
        with self.assertRaises(CommandException):
            self.command.execute(self.empty_problem)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
