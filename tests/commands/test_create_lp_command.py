import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_lp_command import CreateLPCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateLPCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
            | CreateBoardCommand() \
            | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = CreateLPCommand()


    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.lp)


    @property
    def representation(self) -> str:
        return "CreateLPCommand('board', 'config', 'constraints', 'solver', 'lp')"

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
