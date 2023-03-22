import unittest
from pathlib import Path

from src.commands.answer_command import AnswerCommand
from tests.commands.test_command import TestCommand


class TestAnswerCommand(TestCommand):

    def setUp(self) -> None:
        self.command = AnswerCommand(Path("problems\\easy\\problem001.yaml"))

    def test_config(self):
        self.assertEqual(Path("problems\\easy\\problem001.yaml"), self.command.config_filename)

    @property
    def output(self) -> Path:
        return Path("output\\answer\\problem001.svg")

    def clazz(self):
        return self.command.__class__.__name__

    @property
    def representation(self) -> str:
        return f"{self.clazz()}('problems\\easy\\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
