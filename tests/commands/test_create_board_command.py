"""TestCreateBoardCommand."""
import unittest
from pathlib import Path

from src.commands.create_board_command import CreateBoardCommand
from src.commands.file_reader_command import FileReaderCommand
from src.commands.load_config_command import LoadConfigCommand
from tests.commands.test_simple_command import TestSimpleCommand


class TestCreateBoardCommand(TestSimpleCommand):
    """Test suite for the CreateBoardCommand class."""

    def setUp(self) -> None:
        """Set up the test environment."""
        super().setUp()
        self.prerequisites = FileReaderCommand(file_name='config_file_name',
                                               target='config_text',
                                               file_path=Path('problems\\easy\\problem001.yaml')) \
                             | LoadConfigCommand()

        self.prerequisites.execute(self.problem)
        self.command = CreateBoardCommand()
        self.representation = "CreateBoardCommand('config', 'board')"


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
