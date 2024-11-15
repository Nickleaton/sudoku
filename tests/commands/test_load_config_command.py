"""TestLoadConfigCommand."""
import unittest
from typing import Dict

from src.commands.load_config_command import LoadConfigCommand
from src.commands.problem import Problem
from tests.commands.test_simple_command import TestSimpleCommand


class TestLoadConfigCommand(TestSimpleCommand):
    """Test suite for the LoadConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = LoadConfigCommand(self.path)
        self.problem = Problem()

    @property
    def representation(self) -> str:
        """Return the string representation of the LoadConfigCommand."""
        return r"LoadConfigCommand('problems\\easy\\problem001.yaml', 'config')"

    def test_repr(self):
        """Test the string representation of the command."""
        self.assertEqual(self.representation, repr(self.command))

    def test_execute(self):
        """Test the execute method of LoadConfigCommand."""
        self.command.execute(self.problem)
        self.assertIsNotNone(self.problem.config)
        self.assertIsInstance(self.problem.config, Dict)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
