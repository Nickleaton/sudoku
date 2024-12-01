"""TestValidateConfigCommand."""
import unittest
from pathlib import Path

from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from src.commands.validate_config_command import ValidateConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestValidateConfigCommand(TestSimpleCommand):
    """Test suite for ValidateConfigCommand class."""

    def setUp(self) -> None:
        """Set up the test environment for ValidateConfigCommand.

        This method sets up the problem and prepares the command to be tested.
        """
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand()

        self.prerequisites.execute(self.problem)
        self.command = ValidateConfigCommand()
        self.representation = r"ValidateConfigCommand('config_text', 'config_validation')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
