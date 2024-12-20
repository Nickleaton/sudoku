"""TestLoadConfigCommand."""
import unittest
from pathlib import Path

from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestLoadConfigCommand(TestSimpleCommand):
    """Test suite for the LoadConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name="config_file_name",
                                               target="config_text",
                                               file_path=Path("problems\\easy\\problem001.yaml")
                                               )
        self.prerequisites.execute(self.problem)
        self.command = LoadConfigCommand(
            source='config_text',
            target='config'
        )
        self.representation = r"LoadConfigCommand('config_text', 'config')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
