"""TestConfigWriterCommand."""
import unittest

from src.commands.config_yaml_to_string_command import ConfigYamlToStringCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestConfigYamlToStringCommand(TestSimpleCommand):
    """Test suite for the ConfigYamlToStringCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.command = ConfigYamlToStringCommand()
        self.representation = 'ConfigYamlToStringCommand()'


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
