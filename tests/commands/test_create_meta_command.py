"""TestCreateMetaCommand."""
import unittest
from pathlib import Path

from src.commands.create_meta_command import CreateMetaCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateMetaCommand(TestSimpleCommand):
    """Test suite for the CreateMetaCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand()
        self.prerequisites.execute(self.problem)
        self.command = CreateMetaCommand()
        self.representation = r"CreateMetaCommand('config', 'meta')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
