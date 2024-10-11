import unittest
from typing import Dict

from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from tests.commands.test_command import TestCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLoadConfigCommand(TestSimpleCommand):

    def setUp(self) -> None:
        super().setUp()
        self.command = LoadConfigCommand(self.path)
        self.problem = Problem()

    @property
    def representation(self) -> str:
        return r"LoadConfigCommand('problems\\easy\\problem001.yaml', 'config')"

    def test_repr(self):
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.config)
        self.assertIsInstance(self.problem.config, Dict)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
