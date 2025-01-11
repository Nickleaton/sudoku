"""TestLoadConfigCommand."""
import unittest

from src.commands.create_config_command import CreateConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateConfigCommand(TestSimpleCommand):
    """Test suite for the CreateConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        # self.prerequisites = LoadConfigFileCommand()
        # self.prerequisites.execute(self.problem)
        self.command = CreateConfigCommand()
        self.representation = 'CreateConfigCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
