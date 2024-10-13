import unittest

from src.commands.create_lp_with_bookkeeping_command import CreateLPWithBookkeepingCommand

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLPWithBookkeepingCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        requirements = LoadConfigCommand(self.path) \
            | CreateBoardCommand() \
            | CreateConstraintsCommand()
        requirements.execute(self.problem)
        self.command = CreateLPWithBookkeepingCommand()

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.linear_program)

    @property
    def representation(self) -> str:
        return r"CreateLPWithBookkeepingCommand('board', 'config', 'constraints', 'solver', 'linear_program')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
