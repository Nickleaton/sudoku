"""TestConfigWriterCommand."""
import unittest
from pathlib import Path

from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.yaml_to_string_command import YamlToStringCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestYamlToStringCommand(TestSimpleCommand):
    """Test suite for the YamlToStringCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name="config_file_name",
                                               target="config_text",
                                               file_path=Path("problems\\easy\\problem001.yaml")
                                               ) \
                             | LoadConfigCommand()
        self.prerequisites.execute(self.problem)
        self.command = YamlToStringCommand()
        self.representation = r"YamlToStringCommand('config', 'config_out')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
