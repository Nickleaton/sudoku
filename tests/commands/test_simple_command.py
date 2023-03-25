import unittest
from pathlib import Path

from src.commands.simple_command import SimpleCommand
from tests.commands.test_command import TestCommand


class TestSimpleCommand(TestCommand):

    def setUp(self) -> None:
        self.command = SimpleCommand(Path("problems\\easy\\problem001.yaml"))

    def test_config(self):
        self.assertEqual(Path("problems\\easy\\problem001.yaml"), self.command.config_filename)

    @property
    def output(self) -> Path:
        return Path("output\\solution\\problem001.txt")

    def clazz(self):
        return self.command.__class__.__name__

    @property
    def representation(self) -> str:
        return f"{self.clazz()}('problems\\easy\\problem001.yaml')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
