import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.lp_command import CreateLPCommand
from src.commands.lp_with_bookkeeping_command import CreateLPWithBookkeepingCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLPWithBookkeepingCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        load_config = LoadConfigCommand(self.path)
        create_board = CreateBoardCommand()
        create_constraints = CreateConstraintsCommand()
        load_config.execute(self.problem)
        create_board.execute(self.problem)
        create_constraints.execute(self.problem)
        self.command = CreateLPWithBookkeepingCommand(True)

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.linear_program)

    @property
    def representation(self) -> str:
        return r"LPWithBookkeepingCommand()"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
