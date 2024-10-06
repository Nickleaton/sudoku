import unittest

from src.commands.command import CommandException
from src.commands.create_board_command import CreateBoardCommand
from src.commands.load_config_command import LoadConfigCommand
from src.items.board import Board
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateBoardCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = CreateBoardCommand()
        self.load_config_command = LoadConfigCommand(self.path)
        self.load_config_command.execute(self.problem)

    @property
    def representation(self) -> str:
        return "CreateBoardCommand()"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.board)
        self.assertIsInstance(self.problem.board, Board)

    def test_exception(self):
        with self.assertRaises(CommandException):
            self.command.execute(self.empty_problem)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
