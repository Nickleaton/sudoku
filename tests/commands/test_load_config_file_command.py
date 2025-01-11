"""TestLoadConfigFileCommand."""
import unittest

from src.commands.load_config_file_command import LoadConfigFileCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLoadConfigFileCommand(TestSimpleCommand):
    """Test suite for the LoadConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = LoadConfigFileCommand()
        self.representation = r"LoadConfigFileCommand()"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
