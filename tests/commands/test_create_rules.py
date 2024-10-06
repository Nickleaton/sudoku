import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.create_rules_command import CreateRulesCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateRulesCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        load_config = LoadConfigCommand(self.path)
        create_board = CreateBoardCommand()
        create_constraints = CreateConstraintsCommand()
        load_config.execute(self.problem)
        create_board.execute(self.problem)
        create_constraints.execute(self.problem)
        self.command = CreateRulesCommand()

    def test_command(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.rules)

    @property
    def representation(self) -> str:
        return r"CreateRulesCommand()"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
