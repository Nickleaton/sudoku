import unittest

from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_constraints_command import CreateConstraintsCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from src.items.item import Item
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateConstraintsCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.load_config = LoadConfigCommand(self.path)
        self.create_board = CreateBoardCommand()
        self.problem = Problem()
        self.load_config.execute(self.problem)
        self.create_board.execute(self.problem)
        self.command = CreateConstraintsCommand()

    @property
    def representation(self) -> str:
        return "CreateConstraintsCommand('config', 'board', 'constraints')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        self.assertIsNotNone(self.problem.config)
        self.assertIsNotNone(self.problem.board)
        self.assertIsNone(self.problem.constraints)

        self.command.execute(self.problem)

        self.assertIsNotNone(self.problem.constraints)
        self.assertIsInstance(self.problem.constraints, Item)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
