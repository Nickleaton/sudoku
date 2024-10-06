import unittest


from src.commands.composed_command import ComposedCommand
from src.commands.create_board_command import CreateBoardCommand
from src.commands.create_problem_command import CreateProblemCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestAnswerCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = AnswerCommand()

    def clazz(self):
        return self.command.__class__.__name__


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
